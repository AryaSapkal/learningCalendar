import unittest
import task
from datetime import datetime
import datetime

class TestWeek(unittest.TestCase):
    def test_week(self):

        test_day: datetime = datetime(2025, 7, 31)

        self.assertEqual(task.Week(test_day).daySentence, "It's July 31, 2025")
        self.assertEqual(task.Week(test_day).habits_this_week, [])



    def test_day(self):
        test_day: datetime = datetime(2025,7,31)
        self.assertEqual(task.Day(test_day).overlaps(task.Day(test_day)),True)




class TestTask(unittest.TestCase):
    def test_task(self):
        another_starting_time = datetime.datetime(2025, 7, 31)

        my_task = task.Task(another_starting_time, datetime.timedelta(hours=2), "Do the laundry", complete=False)
        self.assertEqual(my_task.title, "Do the laundry")
        my_task.title = "Complete HW #6"
        self.assertEqual(my_task.title, "Complete HW #6")