import sqlite3


conn = sqlite3.connect('tasks.db', isolation_level=None)
c = conn.cursor()
with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_name TEXT NOT NULL,
                    description TEXT,
                    start_time TEXT NOT NULL, 
                    duration INTEGER NOT NULL
                    )""")
    #print(f'Here they are:{c.fetchall()}')