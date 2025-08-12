from __future__ import annotations
import task
from task import Task
import datetime
from schedule import Schedule


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
        day.task_list.append(task)



    # update a task



    # delete a task
    def delete_task(self, task: Task):
        self.schedule.remove_task(task)











another_starting_time = datetime.datetime(2025,7,31)

my_task = Task(another_starting_time, datetime.timedelta(hours=2), "Do the laundry", complete=False)
print(my_task.title)
my_task.title = "Complete HW #6"
print(my_task.title)