from task import Task
from taskManager import TaskManager
import datetime
import sqlite3


def main():
    my_task_manager = TaskManager()

    my_task = Task(datetime.datetime(2025, 8, 27), datetime.timedelta(hours=2), "Do the laundry", complete=False)
    #my_schedule = Schedule()
    my_task_manager.schedule.create_task(my_task)

    conn = sqlite3.connect('tasks.db', isolation_level=None)
    c = conn.cursor()
    with conn:
        c.execute(f"SELECT * FROM tasks WHERE id={my_task.db_id}")
        #print(f'Here they are:{c.fetchall()}')


if __name__ == '__main__':
    main()




