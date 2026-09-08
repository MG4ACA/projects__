import csv
import io
import math
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

import pandas as pd
import requests
import streamlit as st

sys.path.insert(0, str(Path(__file__).parent))
import db
from prompt_builder import BOARDS, build_generation_prompt, default_start_date, display_date


st.set_page_config(page_title="Post Idea Studio", page_icon="P", layout="wide")
db.init_db()


def keywords(description):
    return ", ".join(dict.fromkeys(re.findall(r"#[A-Za-z0-9]+", description or "")))


def iso_publish_date(value):
    text = str(value).replace("—", "-").strip()
    text = re.sub(r"^Day \d+\s*-\s*", "", text)
    for pattern in ("%A %B %d, %Y", "%a %b %d"):
        try:
            parsed = datetime.strptime(text, pattern)
            return parsed.date().isoformat() if "%Y" in pattern else date(2026, parsed.month, parsed.day).isoformat()
        except ValueError:
            continue
    try:
        return date.fromisoformat(text).isoformat()
    except ValueError:
        return ""


def direct_media_url(value):
    """Convert a shared Google Drive file URL to its direct-download equivalent."""
    value = str(value).strip()
    match = re.search(r"drive\.google\.com/file/d/([^/?]+)", value)
    return f"https://drive.google.com/uc?export=download&id={match.group(1)}" if match else value


def preview_media_url(value):
    """Drive's uc?export=download link returns an HTML page, not raw bytes, when embedded as <img> - use the googleusercontent CDN endpoint instead. Small width keeps the thumbnail lightweight and avoids Drive's rate limit."""
    value = str(value).strip()
    match = re.search(r"[?&]id=([^&]+)", value) or re.search(r"drive\.google\.com/file/d/([^/?]+)", value)
    return f"https://lh3.googleusercontent.com/d/{match.group(1)}=w200" if match else value


@st.cache_data(ttl=3600, max_entries=200)
def fetch_preview_image(value):
    """Download a small preview on the Streamlit server instead of from the browser."""
    file_id = extract_drive_id(value)
    if not file_id:
        return None
    urls = [
        f"https://drive.google.com/thumbnail?id={file_id}&sz=w200",
        f"https://drive.google.com/uc?export=download&id={file_id}",
    ]
    for url in urls:
        try:
            response = requests.get(url, timeout=15)
            content_type = response.headers.get("content-type", "")
            if response.ok and content_type.startswith("image/"):
                return response.content
        except requests.RequestException:
            continue
    return None


def extract_drive_id(value):
    value = str(value).strip()
    match = re.search(r"[?&]id=([^&]+)", value) or re.search(r"drive\.google\.com/file/d/([^/?]+)", value)
    return match.group(1) if match else None


def fetch_drive_filenames(file_ids, api_key):
    """Look up each Drive file's original filename via the Drive API - works for publicly-shared files with just an API key, no OAuth needed."""
    names_by_id = {}
    for file_id in file_ids:
        try:
            response = requests.get(
                f"https://www.googleapis.com/drive/v3/files/{file_id}",
                params={"fields": "name", "key": api_key},
                timeout=10,
            )
            if response.ok:
                names_by_id[file_id] = response.json().get("name", "")
        except requests.RequestException:
            continue
    return names_by_id


def export_csv(rows, batch_version, drive_urls):
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=["Title", "Media URL", "Pinterest board", "Thumbnail", "Description", "Link", "Publish date", "Keywords"])
    writer.writeheader()
    for row in rows:
        number = int(row["post_number"])
        board = row["board"]
        base_url = "https://lumicore-labs.com/" if board == "Build. Scale. Ship. — Software Studio" else "https://www.pinterest.com/wildbuild/"
        writer.writerow({
            "Title": row["title"],
            "Media URL": direct_media_url(drive_urls[number]),
            "Pinterest board": board,
            "Thumbnail": "",
            "Description": row["description"],
            "Link": f"{base_url}?utm_source=pinterest&utm_medium=bulk_upload&utm_campaign={batch_version}_pin_{number:02d}",
            "Publish date": iso_publish_date(row["posting_day"]),
            "Keywords": keywords(row["description"]),
        })
    return output.getvalue().encode("utf-8")


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
STOPWORDS = {
    "the", "and", "with", "for", "from", "your", "this", "that", "into", "onto",
    "over", "under", "near", "2026", "visible", "people", "cinematic", "style",
    "photo", "photography", "hyper", "realistic", "vertical",
}


def slugify(value):
    value = re.sub(r"[^A-Za-z0-9]+", "_", str(value)).strip("_")
    return re.sub(r"_+", "_", value)


def tokenize(text):
    words = re.findall(r"[a-z]{4,}", str(text).lower())
    return {word for word in words if word not in STOPWORDS}


def filename_tokens(path):
    stem = re.sub(r"[_\-]?\d{6,}$", "", path.stem)
    return tokenize(stem.replace("_", " ").replace("-", " "))


def auto_match_images(rows, files):
    """Greedy best-first matching by shared keywords between Title/AI Prompt and filename."""
    row_tokens = {row["post_number"]: tokenize(row["title"]) | tokenize(row.get("ai_prompt", "")) for row in rows}
    file_tokens = {path: filename_tokens(path) for path in files}
    candidates = sorted(
        (
            (len(rtoks & ftoks), number, path)
            for number, rtoks in row_tokens.items()
            for path, ftoks in file_tokens.items()
            if rtoks & ftoks
        ),
        key=lambda item: item[0],
        reverse=True,
    )
    matched, used_files = {}, set()
    for score, number, path in candidates:
        if number not in matched and path not in used_files:
            matched[number] = (path, score)
            used_files.add(path)
    return matched


def build_image_rename_preview(folder, rows, matches):
    return pd.DataFrame([
        {
            "Post #": row["post_number"],
            "Title": row["title"],
            "Current filename": matches[row["post_number"]][0].name if row["post_number"] in matches else "",
            "Match score": matches[row["post_number"]][1] if row["post_number"] in matches else 0,
        }
        for row in rows
    ])


def build_rename_plan(folder, rows, edited_frame, batch_version):
    plan, seen_sources = [], {}
    for row in rows:
        number = int(row["post_number"])
        selected_name = edited_frame.loc[edited_frame["Post #"] == number, "Current filename"].iloc[0]
        source = Path(folder) / selected_name if selected_name else None
        reason = ""
        if not selected_name:
            reason = "No file selected"
        elif not source.is_file():
            reason = "File not found"
            source = None
        elif selected_name in seen_sources:
            reason = f"Also selected by post {seen_sources[selected_name]}"
            source = None
        else:
            seen_sources[selected_name] = number
            reason = "Ready"
        suffix = source.suffix.lower() if source else ".jpeg"
        target = Path(folder) / f"{batch_version}_{number:02d}_{slugify(row['title'])}{suffix}"
        plan.append({"Post #": number, "Title": row["title"], "Current filename": selected_name, "New filename": target.name, "Result": reason, "Source": source, "Target": target})
    return plan


st.title("Post Idea Studio")
st.caption("Prepare prompts, review generated ideas, and export Pinterest bulk CSVs locally.")

generate_tab, review_tab, rename_tab, export_tab = st.tabs(["Generate prompt", "Review ideas", "Rename images", "Export bulk CSV"])

with generate_tab:
    st.subheader("Batch settings")
    with st.form("generation_form"):
        left, right = st.columns(2)
        with left:
            version = st.text_input("Version", value="v27")
            start_date = st.date_input("Day 1", value=default_start_date())
            days = st.number_input("Number of days", min_value=1, max_value=14, value=5)
        with right:
            pins_per_day = st.number_input("Pins per day", min_value=1, max_value=20, value=6)
            selected_boards = st.multiselect("Boards", BOARDS, default=BOARDS)
            theme_notes = st.text_area("Theme or campaign notes", placeholder="Halloween, lead generation, seasonal campaign...")
        submitted = st.form_submit_button("Build generation prompt", type="primary")
    if submitted:
        if not selected_boards:
            st.error("Select at least one board.")
        else:
            prompt = build_generation_prompt(start_date, days, pins_per_day, version, theme_notes, selected_boards)
            st.session_state["generation_prompt"] = prompt
            st.success(f"Prompt ready for {days * pins_per_day} pins, ending {display_date(start_date + timedelta(days=days - 1))}.")
    if st.session_state.get("generation_prompt"):
        st.text_area("Copy this into Copilot or Antigravity", st.session_state["generation_prompt"], height=420)

with review_tab:
    st.subheader("Load generated planning CSV")
    upload = st.file_uploader("Planning CSV", type="csv", key="planning_upload")
    if upload:
        frame = pd.read_csv(upload)
        st.write(f"Loaded {len(frame)} rows.")
        version_match = re.search(r"_v(\d+(?:-part\d+)?)", upload.name)
        review_version = st.text_input("Batch version", value=f"v{version_match.group(1)}" if version_match else "v27", key="review_version")
        edited = st.data_editor(frame, width="stretch", num_rows="dynamic", height=500)
        if st.button("Save batch to SQLite", type="primary"):
            required = {"Post #", "Pinterest board", "Title", "Description", "Posting Day", "Slot", "SL Post Time"}
            missing = required - set(edited.columns)
            if missing:
                st.error(f"Missing columns: {', '.join(sorted(missing))}")
            elif not review_version.strip():
                st.error("Batch version is required.")
            else:
                version = review_version.strip()
                start = date.today().isoformat()
                batch_id = db.upsert_batch(version, start, start, 1, len(edited), len(edited), ", ".join(edited["Pinterest board"].dropna().unique()), "")
                db.replace_post_ideas(batch_id, [{
                    "post_number": int(row["Post #"]), "board": row["Pinterest board"], "title": row["Title"],
                    "description": row["Description"], "alt_text": row.get("Alt Text", ""), "ai_prompt": row.get("AI Prompt", ""),
                    "in_app_text_hook": row.get("In-App Text Hook", ""), "posting_day": row["Posting Day"],
                    "slot": row["Slot"], "sl_post_time": row["SL Post Time"], "status": row.get("Status", "Ready"),
                } for _, row in edited.iterrows()])
                st.success(f"Saved {len(edited)} ideas to batch {version}.")

with rename_tab:
    st.subheader("Rename generated images by post number")
    st.caption("Load the planning CSV, review the auto-matched filenames, override any row using the dropdown, then rename.")
    rename_csv = st.file_uploader("Planning CSV", type="csv", key="rename_planning_upload")
    image_folder = st.text_input("Image folder path", placeholder=r"C:\path\to\assets\images\v27")
    rename_version = st.text_input("Batch version", value="v27", key="rename_version")
    if rename_csv and image_folder:
        rename_frame = pd.read_csv(rename_csv)
        required = {"Post #", "Title"}
        missing = required - set(rename_frame.columns)
        folder = Path(image_folder).expanduser()
        if missing:
            st.error(f"Missing columns: {', '.join(sorted(missing))}")
        elif not folder.is_dir():
            st.error("Image folder does not exist.")
        else:
            rename_rows = [
                {"post_number": int(row["Post #"]), "title": row["Title"], "ai_prompt": row.get("AI Prompt", "")}
                for _, row in rename_frame.iterrows()
            ]
            files = [path for path in folder.iterdir() if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS]
            matches = auto_match_images(rename_rows, files)
            st.write(f"Auto-matched {len(matches)} of {len(rename_rows)} posts to {len(files)} image files by keyword overlap.")
            preview = build_image_rename_preview(folder, rename_rows, matches)
            file_options = [""] + sorted(path.name for path in files)
            editor_key = f"rename_editor_{rename_csv.name}_{rename_csv.size}_{folder}_{rename_version}_{len(rename_rows)}"
            edited_preview = st.data_editor(
                preview,
                width="stretch",
                hide_index=True,
                disabled=["Post #", "Title", "Match score"],
                column_config={"Current filename": st.column_config.SelectboxColumn("Current filename", options=file_options)},
                key=editor_key,
            )
            plan = build_rename_plan(folder, rename_rows, edited_preview, rename_version)
            result_preview = pd.DataFrame([{key: item[key] for key in ("Post #", "Title", "Current filename", "New filename", "Result")} for item in plan])
            st.dataframe(result_preview, width="stretch", hide_index=True)
            unresolved = [item for item in plan if item["Result"] != "Ready"]
            existing_targets = [item["Target"].name for item in plan if item["Target"].exists() and item["Target"] != item["Source"]]
            if unresolved:
                st.error(f"{len(unresolved)} image mapping(s) need attention before renaming.")
            elif existing_targets:
                st.error(f"Target already exists: {', '.join(existing_targets)}")
            elif st.button("Rename images", type="primary"):
                for item in plan:
                    item["Source"].rename(item["Target"])
                st.success(f"Renamed {len(plan)} images in {folder}.")

with export_tab:
    st.subheader("Create Pinterest bulk-upload CSV")
    batches = db.list_batches()
    if not batches:
        st.info("Save a planning CSV in Review ideas first.")
    else:
        labels = [batch["version"] for batch in batches]
        selected_version = st.selectbox("Batch", labels)
        batch = db.get_batch(selected_version)
        rows = db.get_post_ideas(batch["id"])
        st.write(f"{len(rows)} saved ideas in {selected_version}.")
        links_text = st.text_area(
            "Drive URLs — either 'post number,url' per line, or a plain comma/newline-separated list assigned in post-number order",
            placeholder="1,https://drive.google.com/uc?export=download&id=...\n2,https://drive.google.com/uc?export=download&id=...",
        )
        drive_urls = {}
        for line in links_text.splitlines():
            match = re.match(r"\s*(\d+)\s*,\s*(\S+)", line)
            if match:
                drive_urls[int(match.group(1))] = match.group(2).strip()
        if not drive_urls:
            plain_urls = [url.strip() for url in re.split(r"[,\n]", links_text) if url.strip()]
            for number, url in zip(sorted(row["post_number"] for row in rows), plain_urls):
                drive_urls[number] = url

        with st.expander("Auto-match images to posts by their original Drive filename (recommended)"):
            st.caption(
                "Instead of relying on the order links were copied in, this looks up each file's real name via the "
                f"Drive API and matches it using the '{selected_version}_NN_...' pattern from the Rename images step."
            )
            api_key = st.text_input("Google Drive API key", type="password", key=f"drive_api_key_{selected_version}")
            raw_urls = [url.rstrip(",") for url in re.findall(r"https?://\S*drive\.google\.com/\S+", links_text)]
            if st.button("Auto-match by filename", disabled=not (api_key and raw_urls)):
                file_ids = [extract_drive_id(url) for url in raw_urls]
                url_by_id = {extract_drive_id(url): url for url in raw_urls}
                names_by_id = fetch_drive_filenames([f for f in file_ids if f], api_key)
                pattern = re.compile(rf"{re.escape(selected_version)}_(\d+)_")
                matched, unmatched = 0, []
                for file_id, name in names_by_id.items():
                    number_match = pattern.search(name)
                    if number_match:
                        st.session_state[f"export_url_{selected_version}_{int(number_match.group(1))}"] = url_by_id[file_id]
                        matched += 1
                    else:
                        unmatched.append(name or file_id)
                st.success(f"Matched {matched} of {len(names_by_id)} images by filename.")
                if unmatched:
                    st.warning(f"Couldn't parse a post number from: {', '.join(unmatched)}")

        st.divider()
        st.subheader("Preview before export")
        st.caption(
            "Drive's 'copy links' order isn't guaranteed to match post order. "
            "Check every thumbnail against its title/description below, and fix the Drive URL on any mismatched row before generating the CSV."
        )
        sorted_rows = sorted(rows, key=lambda row: row["post_number"])
        columns_per_row = 10
        with st.form(f"preview_form_{selected_version}"):
            for start in range(0, len(sorted_rows), columns_per_row):
                for col, row in zip(st.columns(columns_per_row), sorted_rows[start:start + columns_per_row]):
                    number = row["post_number"]
                    with col:
                        st.markdown(f"**#{number}**  \n{row['title']}")
                        url = st.session_state.get(f"export_url_{selected_version}_{number}", drive_urls.get(number, ""))
                        if url:
                            image_bytes = fetch_preview_image(url)
                            if image_bytes:
                                st.image(image_bytes, width="stretch")
                            else:
                                st.error("Could not load image preview — check the URL.")
                        else:
                            st.warning("No Drive URL assigned.")
                        st.text_input(
                            "Drive URL", value=url, key=f"export_url_{selected_version}_{number}", label_visibility="collapsed"
                        )
                        description = row["description"]
                        st.caption(description[:60] + ("…" if len(description) > 60 else ""))
            st.form_submit_button("Apply URL edits")
        for row in sorted_rows:
            number = row["post_number"]
            edited_value = st.session_state.get(f"export_url_{selected_version}_{number}")
            if edited_value is not None:
                drive_urls[number] = edited_value.strip()

        missing = [row["post_number"] for row in rows if not drive_urls.get(row["post_number"])]
        if missing:
            st.warning(f"Missing Drive URLs for {len(missing)} posts.")
        if st.button("Prepare bulk CSV", type="primary", disabled=bool(missing)):
            data = export_csv(rows, selected_version, drive_urls)
            st.download_button("Download Pinterest CSV", data, f"Pinterest_BulkUpload_{selected_version}.csv", "text/csv")
