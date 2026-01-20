import sqlite3

DB_PATH="tasks.db"

def get_db():
    conn=sqlite3.connect(DB_PATH)
    conn.row_factory=sqlite3.Row
    return conn

def init_db():
    conn=get_db()
    cur=conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS task_manager (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    status INTEGER DEFAULT 0,
    task_date DATE DEFAULT CURRENT_DATE,
    priority INTEGER DEFAULT 1,
    reminder_at TIMESTAMP,
    archived INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP
);
""")
    conn.commit()
    cur.close()
    conn.close()
