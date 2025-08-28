from __future__ import annotations
import task
from task import Task
import datetime
from schedule import Schedule
import sqlite3


conn = sqlite3.connect('tasks.db', isolation_level=None)

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS tasks (task_name text, time_start text, duration text, description text)")

some_desciption = "Here is some description."

"""c.execute("INSERT INTO tasks VALUES (:task_name, :time_start, :duration, :description)",
{'task_name':'Do the laundry',
            'time_start':f'{datetime.datetime.now().strftime("%A, %B %d, %Y %H:%M:%S")}',
            'duration':str(datetime.timedelta(hours=2)),
            'description': some_desciption})"""

c.execute("SELECT * FROM tasks")

print(c.fetchall())

conn.close()


class TaskManager:
    """Creates, reads, updates, and deletes Tasks from a Schedule"""
    def __init__(self):
        self.tasks = []
        self.schedule = Schedule()



    # create a task and input it into the Schedule
    def create_task(self, schedule: Schedule, time_start: datetime.datetime, duration: datetime.timedelta, title: str, description: str, complete: bool = None, priority: int = None):
        new_task = Task(time_start, duration, title, description, complete, priority)
        schedule.task_list.append(new_task)



    





    # Adding task should only take in one argument, which is task. The task object will already contain the time for which it is to be done
    def add_task(self, day: task.Day, task: task.Task):
        for t in self.tasks:
            if task.overlaps(t):
                raise ValueError(f"{task.name} overlaps with {t.name}")
        self.schedule.add_task(task)
        #self.tasks.append(task)



    # update a task



    # delete a task
    def delete_task(self, task: Task):
        self.schedule.remove_task(task)


    def write_calendar(self):
        with open("schedule.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task.name}")











