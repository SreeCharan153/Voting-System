from sqlite3 import connect
from pathlib import Path


DB_DIR = Path('./Database')
DB_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = DB_DIR / 'voting.db'


INIT_SQL = """
PRAGMA foreign_keys = ON;


CREATE TABLE IF NOT EXISTS parties (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL UNIQUE,
votes INTEGER NOT NULL DEFAULT 0,
party_president TEXT NOT NULL,
party_candidate TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS VoterList (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
password_hash TEXT NOT NULL,
voting_state INTEGER NOT NULL DEFAULT 0
);


CREATE TABLE IF NOT EXISTS meta (
k TEXT PRIMARY KEY,
v TEXT
);
"""




def get_conn():
    return connect(str(DB_PATH))




def init_db():
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.executescript(INIT_SQL)
        conn.commit()




# Initialize DB on import (idempotent)
init_db()