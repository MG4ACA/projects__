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
    match = re.search(r"[A-Z][a-z]{2} ([A-Z][a-z]{2}) (\d{1,2})", str(value))
    if match:
        month = datetime.strptime(match.group(1), "%b").month
        return date(2026, month, int(match.group(2))).isoformat()
    try:
        return date.fromisoformat(str(value)).isoformat()
    except ValueError:
        return ""


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
            "Media URL": drive_urls[number],
            "Pinterest board": board,
            "Thumbnail": "",
            "Description": row["description"],
            "Link": f"{base_url}?utm_source=pinterest&utm_medium=bulk_upload&utm_campaign={batch_version}_pin_{number:02d}",
            "Publish date": iso_publish_date(row["posting_day"]),
            "Keywords": keywords(row["description"]),
        })
    return output.getvalue().encode("utf-8")


st.title("Post Idea Studio")
st.caption("Prepare prompts, review generated ideas, and export Pinterest bulk CSVs locally.")

generate_tab, review_tab, export_tab = st.tabs(["Generate prompt", "Review ideas", "Export bulk CSV"])

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