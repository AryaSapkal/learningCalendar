from task import Task
import sqlite3

class Schedule:
    def __init__(self):
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


    def create_task(self, task: Task):
        conn = sqlite3.connect('tasks.db', isolation_level=None)
        c = conn.cursor()
        with conn:
            c.execute("INSERT INTO tasks VALUES (:id, :task_name, :description, :start_time, :duration)",
                  {'id': task.db_id,
                      'task_name': task.name,
                   'description': task.description,
                   'start_time': str(task.time_start),
                   'duration': str(task.duration),
                   })
            id = c.lastrowid
        task.db_id = id



    def update_task(self, task: Task):
        conn = sqlite3.connect('tasks.db', isolation_level=None)
        c = conn.cursor()
        with conn:
            c.execute(f"""UPDATE tasks
                        SET task_name = {task.title}, time_start = {task.time_start}, duration = {task.duration}, description = {task.description}
                        WHERE id={task.db_id}
            """)



    def delete_task(self, task: Task):
        conn = sqlite3.connect('tasks.db', isolation_level=None)
        c = conn.cursor()
        with conn:
            c.execute(f"DELETE FROM tasks WHERE id={task.db_id}")






