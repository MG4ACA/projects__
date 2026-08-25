import csv
import re
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "pinterest-post-generation" / "post-ideas" / "Pinterest_Halloween_PostIdeas_Aug25_Aug29_v25-halloween.csv"
OUTPUT = ROOT / "pinterest-post-generation" / "bulk-uploads" / "Pinterest_BulkUpload_Aug25_Aug29_v25-halloween.csv"
CAMPAIGN = "halloween_2026"
DRIVE_IDS = {
    1: "1s2LOOAbeH5O4xE2Y8z2XHzAgPW60e2xF",
    2: "1yr6pbLWNEj3zz33SnQiY2gM4zszwgnxW",
    3: "13QNA00TOkJv66OiVRroRQ1XZYmZtYDea",
    4: "1l2RRvETu29PJISRcdiJKCr3KW7eDWJxi",
    5: "10ofSjIdoWiJSHLVnds-iws7vmyzwQ6Ft",
    6: "1dcSWwU0h7LVqShjJ4cVefx6ZM3S5_VVH",
    7: "10TFEuuzcOA8NJt28ZIuHqSU0BEjicVhj",
    8: "1tG8AdTy2Gro61mO6vStHAIIVwcJHq_rQ",
    9: "17rx6A_Rhy3uViZlLhti7vcvxs5MHFtvn",
    10: "1S_KwutUTcYaWkU2U5GbJl4dz5MuySvJG",
    11: "1HfsOOMr7OwpLgWt4Hw6YoVwaTxpxAK7y",
    12: "1h8m_HwuJrnmBfLg2WvAQraRRZFYRXaqj",
    13: "1p1bVVusgRBaEL1VgKJv4u8rTLzjdN6HV",
    14: "1-sJqzPzwFbtE4Wnf-XYOO13RgL4vy-WG",
    15: "1Aa7tA4pKfvlZtaz7WppeDgWEYMCWZ6iK",
    16: "1t4OHlXl7Vy2dKxjV3sbetSY4dE7q7Lap",
    17: "1p8QLHBv9U1INvnx8O0p9OrZoDfw4IkF_",
    18: "1j0VQnHRtrsx2fVvfCvLmLcVtMfu6xYtx",
    19: "114kvIqoz8tWorTSl8d39BXdD4VLorf8A",
    20: "1b3bohS2S92nKqlfffYk-F61guniVq4H5",
    21: "17vCuEAoDIvMbxGXH6JEmwAre2xwH0v-q",
    22: "1I5c2F_0EELeWddmoK54DySMnZRg51OR-",
    23: "1h23DC9WaPCLc5ZL6NSMrVEZorOaCifcM",
    24: "1ML8m6BuDAoY-0fuiujZAXg8GEC1vLeCU",
    25: "12PhZ4ZHwXn3ObKfrlmMDwe5MWjMfxwWF",
    26: "1yby41iSlEb-nnU40ubhec27PecbXX3lF",
    27: "1geK8JtUrwtB9YbCjI40AI2aE4wacnuRY",
    28: "1azPpRjPWG9BhhPczbFPIRW1AucS5GvpR",
    29: "1vHbIv_ms1428oEPsMD2VFaBvFs1S5C-X",
    30: "1Y82tCW8xwytnyzosByrbDfn2mKpgMwH_",
}


def keywords(description):
    return ", ".join(dict.fromkeys(re.findall(r"#[A-Za-z0-9]+", description)))


def publish_date(posting_day):
    match = re.search(r"[A-Z][a-z]{2} ([A-Z][a-z]{2}) (\d{1,2})", posting_day)
    if not match:
        return ""
    return datetime.strptime(
        f"{match.group(1)} {match.group(2)} 2026", "%b %d %Y"
    ).strftime("%Y-%m-%d")


with SOURCE.open(newline="", encoding="utf-8-sig") as source_file:
    rows = csv.DictReader(source_file)
    required_columns = {"Post #", "Pinterest board", "Title", "Description", "Posting Day"}
    missing_columns = required_columns - set(rows.fieldnames or [])
    if missing_columns:
        raise ValueError(f"Missing planning columns: {', '.join(sorted(missing_columns))}")

    bulk_rows = []
    for row in rows:
        post_number = int(row["Post #"])
        description_keywords = keywords(row["Description"])
        if not description_keywords:
            raise ValueError(f"Post {post_number} has no hashtags for Keywords")
        bulk_rows.append(
            {
                "Title": row["Title"],
                "Media URL": f"https://drive.google.com/uc?export=download&id={DRIVE_IDS[post_number]}",
                "Pinterest board": row["Pinterest board"],
                "Thumbnail": "",
                "Description": re.sub(r"\s*https://future\.lumicore-labs\.com/halloween", "", row["Description"]),
                "Link": "",
                "Publish date": publish_date(row["Posting Day"]),
                "Keywords": description_keywords,
            }
        )

with OUTPUT.open("w", newline="", encoding="utf-8-sig") as output_file:
    writer = csv.DictWriter(
        output_file,
        fieldnames=[
            "Title",
            "Media URL",
            "Pinterest board",
            "Thumbnail",
            "Description",
            "Link",
            "Publish date",
            "Keywords",
        ],
    )
    writer.writeheader()
    writer.writerows(bulk_rows)

print(f"Created {OUTPUT} with {len(bulk_rows)} rows")
