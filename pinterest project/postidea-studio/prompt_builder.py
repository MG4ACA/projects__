from datetime import date, timedelta


BOARDS = [
    "Future Living & Off-Grid Tech",
    "Smart Pet Wellness | Eco-Tech & Quiet Luxury",
    "Build. Scale. Ship. — Software Studio",
    "Halloween Home Decor & DIY",
]


def build_generation_prompt(start_date, days, pins_per_day, version, theme_notes, selected_boards):
    end_date = start_date + timedelta(days=days - 1)
    board_text = ", ".join(selected_boards)
    return f"""Role: You are a Pinterest Growth Scientist and AI Content Strategist for @wildbuild.

Generate a {days}-day batch with {pins_per_day} pins per day ({days * pins_per_day} total pins).
Batch version: {version}
Day 1: {display_date(start_date)}
Day {days}: {display_date(end_date)}
Active boards: {board_text}

Follow pinterest-post-generation/Content-Brief-for-Claude.md exactly.
Read the latest analytics and audience CSVs before writing.
Use the exact board names above. Generate the internal planning CSV with this exact header:
\"Post #\",\"Pinterest board\",\"Title\",\"Description\",\"Alt Text\",\"AI Prompt\",\"In-App Text Hook\",\"Status\",\"Posting Day\",\"Slot\",\"SL Post Time\"

Theme or campaign notes:
{theme_notes or 'Use the strongest current themes from analytics.'}

Save the CSV to pinterest-post-generation/post-ideas/ using the established filename convention. Do not print the full CSV in chat."""


def default_start_date():
    return date.today() + timedelta(days=1)


def display_date(value):
    return value.strftime("%A, %B %d, %Y").replace(" 0", " ")