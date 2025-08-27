from task import Task
import sqlite3

class Schedule:
    def __init__(self):
        #self.timeline = []
        #self.task_list = []
        conn = sqlite3.connect('tasks.db', isolation_level=None)
        c = conn.cursor()
        with conn:
            c.execute("""CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_name TEXT NOT NULL,
                    description TEXT,
                    start_time TEXT NOT NULL, 
                    duration INTEGER NOT NULL""")


    def add_task(self, task: Task):
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()
        with conn:
            c.execute("INSERT INTO tasks VALUES (:task, :task_name, :time_start, :duration, :description)",
                  {'task': task.db_id,
                      'task_name': task.name,
                   'time_start': str(task.time_start),
                   'duration': str(task.duration),
                   'description': task.description})
            id = c.lastrowid
        task.__db_id = id


    def remove_task(self, task: Task):
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()
        with conn:
            c.execute("DELETE FROM tasks WHERE ")

        if task in self.task_list:
            self.task_list.remove(task)

