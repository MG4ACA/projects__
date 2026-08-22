import csv
import re
from datetime import datetime


SOURCE = "Pinterest_Next30_PostIdeas_Aug23_Aug27_v25.csv"
OUTPUT = "Pinterest_BulkUpload_Aug23_Aug27_v25.csv"
DESTINATION = "https://www.pinterest.com/wildbuild/"
SOFTWARE_DESTINATION = "https://lumicore-labs.com/"
DRIVE_IDS = {
    1: "1Jou1nrL9U9z9HMPRKuwpcg8Ti-9JTrcG",
    2: "1TVCmGNku7aq5F44ECswSB6OaSFf_-105",
    3: "17euRJWx34RsUNz-tnPqUqqqUDZ0BVzTD",
    4: "1TaoPPgNiJIXU38WBgOslxR_3hiRBh2vW",
    5: "1vDMJrF-9248bgvnfBCAzDotRELByl3dg",
    6: "1lGnpzv0NymB3zXN25Mtf6aQcA7ZOXCuJ",
    7: "1iFPqDh3PuE-4fA-PlNmMgLU8EJnN2KBr",
    8: "1KC8OghnaXjibVy0MViOxTEXc2aZ6AwNr",
    9: "12y9qc0tcfIaJCA0qwiRa4t8YxIV46B4t",
    10: "1BkW6gcIZf18RyYKs037YITDQmsLF7QAu",
    11: "1iy-v3FzGPF4CpZJ934XQyu0Y2_qtbXl9",
    12: "1Yc6EsC9M3T6oWR7kFobb7NdRxIsXgdoq",
    13: "1B161s2tsQd7hTzawKj_IxRpeqxrryKq5",
    14: "1whc73Hm7qRoIvKbx_8UtVM8SmTvLjbAb",
    15: "1Y8n0i9DIzj_3r7xXBdirJqbJk_waDlS-",
    16: "16EIgPBxDllnyb8Otbt3cx2L4Zwaw-4GV",
    17: "1v__AGPtKAlgEdKBKg1f2JWFy0n-waVvw",
    18: "1eTQgZLTgK625XADCT698n2rPdw2e_XyJ",
    19: "1Wzet0yx5WGnNolxTQ6n_cxzspXt9lXR2",
    20: "1dg0fgt31cOH7gU5ee0XsERipgrhOLufv",
    21: "1KRUiYCfze-2txpAcecEeSg8890jSJ_Kn",
    22: "1320EzWyT7Iemafewsx8MWhNwTgYLphnk",
    23: "1vXI_bkUC1ZBlMnm5e5glLFuWZQB3mwd_",
    24: "1YRXVqsJIgzK_C2_6lQo6BPQbQKcpoAqv",
    25: "1tQ22sZtMCXxXGAtGhrL9cmOnyqC3FDwS",
    26: "18tlSSKFt5f-Ricbn9B6lrTenONK78KHm",
    27: "1lpIgI5CV4aElxPRLWpzukxec16zkxUv7",
    28: "1pba2faoSAxmjo12dgh-A2dy2ZsofaUJH",
    29: "1t0MIqbvyfZAwfNUP0LMNt4EP_aOTah3x",
    30: "1k4R24ksgWAyf70W1Uw2R2LOMHN0dHvZ3",
}


def keywords(description):
    return ", ".join(dict.fromkeys(re.findall(r"#[A-Za-z0-9]+", description)))


def publish_date(posting_day):
    match = re.search(r"[A-Z][a-z]{2} ([A-Z][a-z]{2}) (\d{1,2})", posting_day)
    if not match:
        return ""
    return datetime.strptime(f"{match.group(1)} {match.group(2)} 2026", "%b %d %Y").strftime("%Y-%m-%d")


def destination(board):
    return SOFTWARE_DESTINATION if board == "Build. Scale. Ship." else DESTINATION


with open(SOURCE, newline="", encoding="utf-8-sig") as source_file:
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
                "Description": row["Description"],
                "Link": destination(row["Pinterest board"]),
                "Publish date": publish_date(row["Posting Day"]),
                "Keywords": description_keywords,
            }
        )

with open(OUTPUT, "w", newline="", encoding="utf-8") as output_file:
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
