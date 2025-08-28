import unittest
from schedule import Schedule
from task import Task
import datetime
import sqlite3


class TestSchedule(unittest.TestCase):

    def test_create_task(self):
        my_task = Task(datetime.datetime(2025, 8, 27), datetime.timedelta(hours=2), "Do the laundry", complete=False)
        my_schedule = Schedule()
        my_schedule.create_task(my_task)

        conn = sqlite3.connect('tasks.db', isolation_level=None)
        c = conn.cursor()
        c.execute(f"SELECT * FROM tasks WHERE id={my_task.db_id}")

        self.assertEqual(c.fetchone(), (my_task.db_id, 'Time: Wednesday, August 27, 2025 12:00 AM\tDuration: 2:00:00\tTask Name: Do the laundry', None, '2025-08-27 00:00:00', '2:00:00'))


    # def test_update_task():



    # def test_delete_task():