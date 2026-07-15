import csv

print("--- AUDIENCE INSIGHTS (July 5) ---")
with open('audience-insights-total-audience-2026-07-05.csv', 'r', encoding='utf-8') as f:
    # get audience size
    reader = csv.reader(f)
    next(reader)
    row = next(reader)
    print(f"Total Audience (July 5): {row[3]}")
    
    # skip empty line and category headers
    next(reader)
    next(reader)
    
    interests = []
    for row in reader:
        if len(row) > 7 and row[4].strip() != '':
            try:
                affinity = float(row[7])
                interests.append((row[4], affinity))
            except ValueError:
                pass
                
    interests.sort(key=lambda x: x[1], reverse=True)
    print("Top 15 Interests (July 5):")
    for interest, aff in interests[:15]:
        print(f"  {interest}: {aff}x")

print("\n--- ANALYTICS OVERVIEW (July 7) ---")
with open('Pinterest Analytics overview 20260607-20260707.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    start_idx = -1
    for i, line in enumerate(lines):
        if line.startswith("Pin ID,"):
            start_idx = i
            break
            
    if start_idx != -1:
        reader = csv.reader(lines[start_idx:])
        headers = next(reader)
        imp_idx = headers.index('Impressions')
        save_idx = headers.index('Saves')
        board_idx = headers.index('Board name')
        
        pins = []
        for row in reader:
            if len(row) > imp_idx:
                try:
                    imp = int(row[imp_idx])
                    saves = int(row[save_idx])
                    pins.append({'board': row[board_idx], 'impressions': imp, 'saves': saves})
                except ValueError:
                    pass
        
        pins.sort(key=lambda x: x['impressions'], reverse=True)
        print("Top 10 Pins by Impressions (June 7 - July 7):")
        for p in pins[:10]:
            print(f"  Board: {p['board']} | Impressions: {p['impressions']} | Saves: {p['saves']}")
            
        # Board totals
        boards = {}
        for p in pins:
            b = p['board']
            if b not in boards:
                boards[b] = {'imp': 0, 'saves': 0}
            boards[b]['imp'] += p['impressions']
            boards[b]['saves'] += p['saves']
            
        print("\nBoard Performance (June 7 - July 7):")
        for b, data in boards.items():
            print(f"  {b}: {data['imp']} impressions, {data['saves']} saves")
