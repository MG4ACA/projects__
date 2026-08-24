import csv, os
from pathlib import Path

top_pins = [
    ('867646684482504284', 12137),
    ('867646684482784961', 10106),
    ('867646684483622373', 9762),
    ('867646684481735030', 9177),
    ('867646684483177976', 7794),
    ('867646684483320177', 6988),
    ('867646684481475922', 6150),
    ('867646684483526037', 5655),
    ('867646684483073529', 5310),
    ('867646684484045188', 2660),
]

folder = Path(__file__).resolve().parent.parent / 'pinterest-post-generation' / 'post-ideas'
csvs = [f for f in os.listdir(folder) if f.startswith('Pinterest_Next') and f.endswith('.csv')]

for pin_id, imp in top_pins:
    found = False
    for csv_file in csvs:
        try:
            with open(os.path.join(folder, csv_file), 'r', encoding='utf-8') as f:
                content = f.read()
                if pin_id in content:
                    f.seek(0)
                    reader = csv.DictReader(f)
                    for row in reader:
                        vals = ' '.join(row.values())
                        if pin_id in vals:
                            keys = list(row.keys())
                            board_key = next((k for k in keys if 'board' in k.lower()), None)
                            title_key = next((k for k in keys if 'title' in k.lower()), None)
                            board = row.get(board_key, 'N/A') if board_key else 'N/A'
                            title = row.get(title_key, 'N/A')[:70] if title_key else 'N/A'
                            print(f"Pin {pin_id}: {imp} impr | {csv_file}")
                            print(f"  Board: {board}")
                            print(f"  Title: {title}")
                            found = True
                            break
                    if found:
                        break
        except Exception as e:
            pass
    if not found:
        print(f"Pin {pin_id}: {imp} impr | NOT FOUND IN POST CSVs")
