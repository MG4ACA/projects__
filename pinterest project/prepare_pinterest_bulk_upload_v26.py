import csv
import re
from datetime import datetime


SOURCE = "pinterest-post-generation/post-ideas/Pinterest_Next60_PostIdeas_Aug30_Sep3_v26.csv"
OUTPUT = "Pinterest_BulkUpload_Aug30_Sep3_v26.csv"
PROFILE_URL = "https://www.pinterest.com/wildbuild/"
SOFTWARE_URL = "https://lumicore-labs.com/"
BOARD_NAMES = {
    "Future Living & Off-Grid Tech": "Future Living & Off-Grid Tech",
    "Smart Pet Wellness": "Smart Pet Wellness | Eco-Tech & Quiet Luxury",
    "Build. Scale. Ship.": "Build. Scale. Ship. — Software Studio",
    "Halloween Home Decor & DIY": "Halloween Home Decor & DIY",
}
DRIVE_IDS = {
    1: "1-71-xgoW_bYwT6KwT7cAZnIhIjS91oLv", 2: "1HjhbMidy7QUvl7xWA_N-FtudmR7WcVAs",
    3: "1BJ99n3Z4DT55eSjbTyBXc1idAg2dDAi3", 4: "1gbEI8TGFUs73XNjPTaWY_fRl5KMfDjBY",
    5: "1et97IEMQdyvyF4-e1_W2ujh5ZBt8fzgT", 6: "1uxP78O143RfvPLV27_G89CP-x_Gb0orI",
    7: "1JUtZzrshZNYJk7qwTDqharMA_crvDULm", 8: "100E0ro5T3pSOZ4JaYPehCVZ7fthNZppM",
    9: "1iKH67kWn4W547H8tK0GOeZXLpgdDPIBC", 10: "1sXRhSjaQrTUDpyGi7z9_6XPFOWsTOWM5",
    11: "1TpU47jjq4pUQYzT0XR6D3O8EHutRVl8_", 12: "1o5EHbaBpoCty7D3Q5B7opFkGL_gIz7cF",
    13: "10mAuGVN9ocqa8x8D53SgK8VNkUohexSx", 14: "1m9MkTnfUfc99YWLFpY2jliJCD_xAASke",
    15: "1ZSLwSGcOqEk6h5KKUG1-CfkgtWeF9uAp", 16: "1zOnzHu5ENpSjLSEZKEKEuvP3PdzK-6jF",
    17: "1BD4wavIvYKonSQTCDPp75AkoyCyEDKGO", 18: "1lorWRhCThNlCYzfI7n325KnXgdR20Dlq",
    19: "1BfD8b2Xn6p2cVso4DBPvQuzzHKxvwkgT", 20: "1ci4z27OHgubkH6Y5s3yWvv8HzdiLiZn1",
    21: "1Bp3Q5KQ3h2l3BqkkMkooCiA0VYBz5PaE", 22: "1L_NZGK-JuUCTChXAcNY-wuwXr8pmjjaW",
    23: "1K-7oW1xt3U4EW3-1_JIdOdMPly3LJ2ng", 24: "1FNDHeanDuRNMZrfBoxangjiA41rGaR1X",
    25: "1VS_h-1hmJslofIEUMKySPw6HXFk-BvdJ", 26: "1eBnSiYErzhNQ7Q3nTa863vxzcrt8j4qO",
    27: "1rozIBGms0IJNiKKwrQbUGzj7ULf5Mttu", 28: "1GGRmdjCE4vurwZr8Q7rLokf6FocqWcMg",
    29: "1CgoCsBU5HvnosIdcqU-lnXkI1V9MTsCw", 30: "1vDIVMNFujs_fSzSQ7cm961ZHrDMHIYjU",
    31: "1x82Eh8rZ4vYjQw3X_6Vt5YviSEBRCEoa", 32: "1ISAhb5JxaxBHT2Zl3cxbg1xiVejLydRH",
    33: "1Fhy-DLwrQYP9KOEaTi4VZ3Wi7ySJHTCe", 34: "1aIcN5Vo8js6X5TkJbCDxVQDGQqRoa8Ph",
    35: "1zw2wXxUQsS0Bt-kSXeAlBBN-z11sQ40M", 36: "1wb_RCSw5ob1YCiGZmAGGmZm8Z6nbxEHJ",
    37: "1AgOlW_-rYRbjxqePLGYzpg8EXqAGrRM4", 38: "1F7XN-Qu462jHZe0uH1ktSZ5mEfMcLFFk",
    39: "11BSgRmVlRqrAJYM1cjw-_Zt4kmGj9AHU", 40: "10vq_ZGI_1wGTXrniXIQiTu6LscEL4fef",
    41: "1_pdheJS1f1uAcjunsHkCR5oefdK_ZnY2", 42: "1iSYvAs8_3XDzJEYFWwMdpkkla2I6SZCf",
    43: "1mhdQ2NWObN6GysdzuDlYn7IICSGOZIZB", 44: "1QOJUly4zoiymOZ29KQTvIZKza43Ti6jf",
    45: "1I51MFJuUgYmH17lHHuKA6CyFK2xMG369", 46: "14Vf_cyydzZCp7rLbJXR8h9ruOuKIdhb-",
    47: "1jK1rFSpxpA3DekT-p0-Ixcg3iVCjbPpq", 48: "1QKnxJPzhlCU2K9aQCDx8RP_Xk-_MOXO3",
    49: "1Y2Cb29IOIElTVtKt3UncOyPldUgxignX", 50: "17A9BBkkUj7ZoGU89lZDmBii47DEk1d_i",
    51: "1Av-78L06BObsJcaLybuZdBiQrKcXdEfE", 52: "1IRmLRf_cYIx0mgoi-nbfA7tlMcA3_i4X",
    53: "1Ioqkyi5eh0tHHwLs5uVtjWyyrw1GzurQ", 54: "1Pd423XDczbs5lfwWW1vTRy5egS0z9yhG",
    55: "1aI10vjwWqEdz2pByD5xiv1tzpY-AIk3E", 56: "1clN1VcnUz7XJIqLcojIp6r-sNIpg-bXZ",
    57: "1eThwIYkQyOshyAdfP5jW40eFC_5Y0l9r", 58: "1i99_r2rPn-hjPrlDITUsBXJxsEQuHWwA",
    59: "1vBKn1KDdRWRoHcf-yjTdzaQpdjW9PxbK", 60: "1xyne0sr210yKh-OTVQ_mq3ea6um8yWOe",
}


def keywords(description):
    return ", ".join(dict.fromkeys(re.findall(r"#[A-Za-z0-9]+", description)))


def publish_date(posting_day):
    match = re.search(r"[A-Z][a-z]{2} ([A-Z][a-z]{2}) (\d{1,2})", posting_day)
    return datetime.strptime(f"{match.group(1)} {match.group(2)} 2026", "%b %d %Y").strftime("%Y-%m-%d") if match else ""


with open(SOURCE, newline="", encoding="utf-8-sig") as source_file:
    source_rows = list(csv.DictReader(source_file))

if {int(row["Post #"]) for row in source_rows} != set(range(1, 61)):
    raise ValueError("The planning CSV must contain one row for every post from 1 through 60")

bulk_rows = []
for row in source_rows:
    post_number = int(row["Post #"])
    source_board = row["Pinterest board"]
    if source_board not in BOARD_NAMES:
        raise ValueError(f"Unrecognized board for post {post_number}: {source_board}")
    row_keywords = keywords(row["Description"])
    if not row_keywords:
        raise ValueError(f"Post {post_number} has no hashtags for Keywords")
    base_url = SOFTWARE_URL if source_board == "Build. Scale. Ship." else PROFILE_URL
    bulk_rows.append({
        "Title": row["Title"],
        "Media URL": f"https://drive.google.com/uc?export=download&id={DRIVE_IDS[post_number]}",
        "Pinterest board": BOARD_NAMES[source_board],
        "Thumbnail": "",
        "Description": row["Description"],
        "Link": f"{base_url}?utm_source=pinterest&utm_medium=bulk_upload&utm_campaign=v26_pin_{post_number:02d}",
        "Publish date": publish_date(row["Posting Day"]),
        "Keywords": row_keywords,
    })

with open(OUTPUT, "w", newline="", encoding="utf-8") as output_file:
    writer = csv.DictWriter(output_file, fieldnames=["Title", "Media URL", "Pinterest board", "Thumbnail", "Description", "Link", "Publish date", "Keywords"])
    writer.writeheader()
    writer.writerows(bulk_rows)

print(f"Created {OUTPUT} with {len(bulk_rows)} rows")
