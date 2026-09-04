import csv
import io
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

import pandas as pd
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


IMAGE_HINTS = {
    1: ("glass_cabin_on_alpine_lake",),
    2: ("caracal_standing_in_desert",),
    3: ("salon_booking_system",),
    4: ("autumn_porch_at_blue_hour",),
    5: ("compact_cycling_workshop",),
    6: ("wirehaired_pointing_griffon",),
    7: ("infographic_comparing_spreadshee",),
    8: ("bats_ascending_wall",),
    9: ("toyota_land_cruiser",),
    10: ("lynx_standing_on_mountain",),
    11: ("infographic_comparing_scaling",),
    12: ("styled_shelf_with_heirloom",),
    13: ("floating_sauna_on_lake",),
    14: ("brittany_dog_running_on_dune",),
    15: ("stop_losing_customers_to_follow-up",),
    16: ("decorated_apartment_balcony",),
    17: ("cabin_beside_lake_with_floatplane",),
    18: ("clouded_leopard_on_mossy_branch",),
    19: ("custom_app_removes_admin_work",),
    20: ("candles_and_pumpkins_on_table",),
    21: ("glass_observatory_pod_on_cliff",),
    22: ("cat_resting_on_window_bench",),
    23: ("inventory_visibility_infographic",),
    24: ("halloween_entryway_with_pumpkin",),
}


def slugify(value):
    value = re.sub(r"[^A-Za-z0-9]+", "_", str(value)).strip("_")
    return re.sub(r"_+", "_", value)


def build_image_rename_plan(folder, rows, batch_version):
    files = [path for path in Path(folder).iterdir() if path.is_file() and path.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}]
    plan = []
    used_sources = set()
    for row in rows:
        number = int(row["post_number"])
        matches = [path for path in files if any(hint.lower() in path.name.lower() for hint in IMAGE_HINTS.get(number, ()))]
        source = matches[0] if len(matches) == 1 else None
        target = Path(folder) / f"{batch_version}_{number:02d}_{slugify(row['title'])}{source.suffix.lower() if source else '.jpeg'}"
        reason = "Matched by image hint" if source else "No unique match"
        if source and source in used_sources:
            source = None
            reason = "Source matched more than once"
        if source:
            used_sources.add(source)
        plan.append({"Post #": number, "Title": row["title"], "Current filename": source.name if source else "", "New filename": target.name, "Result": reason, "Source": source, "Target": target})
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
        edited = st.data_editor(frame, use_container_width=True, num_rows="dynamic", height=500)
        if st.button("Save batch to SQLite", type="primary"):
            required = {"Post #", "Pinterest board", "Title", "Description", "Posting Day", "Slot", "SL Post Time"}
            missing = required - set(edited.columns)
            if missing:
                st.error(f"Missing columns: {', '.join(sorted(missing))}")
            else:
                version_match = re.search(r"_v(\d+)", upload.name)
                version = f"v{version_match.group(1)}" if version_match else st.text_input("Batch version", "v27")
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
    st.caption("Load the planning CSV, preview the mapping, then rename the local image files to stable post-number filenames.")
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
            rename_rows = [{"post_number": int(row["Post #"]), "title": row["Title"]} for _, row in rename_frame.iterrows()]
            plan = build_image_rename_plan(folder, rename_rows, rename_version)
            preview = pd.DataFrame([{key: item[key] for key in ("Post #", "Title", "Current filename", "New filename", "Result")} for item in plan])
            st.dataframe(preview, use_container_width=True, hide_index=True)
            unresolved = [item for item in plan if not item["Source"]]
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
        links_text = st.text_area("Drive URLs, one per line as post number,url", placeholder="1,https://drive.google.com/uc?export=download&id=...\n2,https://drive.google.com/uc?export=download&id=...")
        drive_urls = {}
        for line in links_text.splitlines():
            if "," in line:
                number, url = line.split(",", 1)
                if number.strip().isdigit():
                    drive_urls[int(number.strip())] = url.strip()
        missing = [row["post_number"] for row in rows if row["post_number"] not in drive_urls]
        if missing:
            st.warning(f"Missing Drive URLs for {len(missing)} posts.")
        if st.button("Prepare bulk CSV", type="primary", disabled=bool(missing)):
            data = export_csv(rows, selected_version, drive_urls)
            st.download_button("Download Pinterest CSV", data, f"Pinterest_BulkUpload_{selected_version}.csv", "text/csv")
