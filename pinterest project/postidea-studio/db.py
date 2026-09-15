"""SQLite persistence for post-idea batches, individual pins, and export links."""
import sqlite3
from contextlib import contextmanager
from pathlib import Path

DB_PATH = Path(__file__).parent / "postideas.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS batches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    version TEXT NOT NULL UNIQUE,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    days INTEGER NOT NULL,
    pins_per_day INTEGER NOT NULL,
    total_pins INTEGER NOT NULL,
    boards TEXT NOT NULL,
    theme_notes TEXT,
    status TEXT NOT NULL DEFAULT 'draft',
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS post_ideas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    batch_id INTEGER NOT NULL REFERENCES batches(id) ON DELETE CASCADE,
    post_number INTEGER NOT NULL,
    board TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    alt_text TEXT,
    ai_prompt TEXT,
    in_app_text_hook TEXT,
    posting_day TEXT,
    slot TEXT,
    sl_post_time TEXT,
    status TEXT NOT NULL DEFAULT 'draft',
    media_drive_id TEXT,
    notes TEXT,
    landing_page TEXT,
    UNIQUE(batch_id, post_number)
);
"""


@contextmanager
def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    try:
        yield connection
        connection.commit()
    finally:
        connection.close()


def init_db():
    with get_connection() as connection:
        connection.executescript(SCHEMA)
        _migrate(connection)


def _migrate(connection):
    """Add columns introduced after a database file already existed."""
    existing = {row["name"] for row in connection.execute("PRAGMA table_info(post_ideas)")}
    if "landing_page" not in existing:
        connection.execute("ALTER TABLE post_ideas ADD COLUMN landing_page TEXT")


def upsert_batch(version, start_date, end_date, days, pins_per_day, total_pins, boards, theme_notes):
    with get_connection() as connection:
        connection.execute(
            """
            INSERT INTO batches (version, start_date, end_date, days, pins_per_day, total_pins, boards, theme_notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(version) DO UPDATE SET
                start_date=excluded.start_date, end_date=excluded.end_date, days=excluded.days,
                pins_per_day=excluded.pins_per_day, total_pins=excluded.total_pins,
                boards=excluded.boards, theme_notes=excluded.theme_notes
            """,
            (version, start_date, end_date, days, pins_per_day, total_pins, boards, theme_notes),
        )
        return connection.execute("SELECT id FROM batches WHERE version = ?", (version,)).fetchone()["id"]


def list_batches():
    with get_connection() as connection:
        return connection.execute("SELECT * FROM batches ORDER BY id DESC").fetchall()


def get_batch(version):
    with get_connection() as connection:
        return connection.execute("SELECT * FROM batches WHERE version = ?", (version,)).fetchone()


def replace_post_ideas(batch_id, rows):
    """rows: list of dicts keyed by post_number, board, title, description, alt_text,
    ai_prompt, in_app_text_hook, posting_day, slot, sl_post_time, status, landing_page."""
    with get_connection() as connection:
        connection.execute("DELETE FROM post_ideas WHERE batch_id = ?", (batch_id,))
        connection.executemany(
            """
            INSERT INTO post_ideas
                (batch_id, post_number, board, title, description, alt_text, ai_prompt,
                 in_app_text_hook, posting_day, slot, sl_post_time, status, landing_page)
            VALUES (:batch_id, :post_number, :board, :title, :description, :alt_text, :ai_prompt,
                    :in_app_text_hook, :posting_day, :slot, :sl_post_time, :status, :landing_page)
            """,
            [{**row, "batch_id": batch_id, "landing_page": row.get("landing_page", "")} for row in rows],
        )


def update_post_idea_statuses(batch_id, statuses_by_post_number):
    with get_connection() as connection:
        connection.executemany(
            "UPDATE post_ideas SET status = ? WHERE batch_id = ? AND post_number = ?",
            [(status, batch_id, post_number) for post_number, status in statuses_by_post_number.items()],
        )


def update_post_idea_media(batch_id, media_by_post_number):
    with get_connection() as connection:
        connection.executemany(
            "UPDATE post_ideas SET media_drive_id = ? WHERE batch_id = ? AND post_number = ?",
            [(drive_id, batch_id, post_number) for post_number, drive_id in media_by_post_number.items()],
        )


def get_post_ideas(batch_id):
    with get_connection() as connection:
        return connection.execute(
            "SELECT * FROM post_ideas WHERE batch_id = ? ORDER BY post_number", (batch_id,)
        ).fetchall()


def set_batch_status(batch_id, status):
    with get_connection() as connection:
        connection.execute("UPDATE batches SET status = ? WHERE id = ?", (status, batch_id))
