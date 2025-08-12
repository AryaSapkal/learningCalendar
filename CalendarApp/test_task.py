import unittest
import task
from datetime import datetime


class TestWeek(unittest.TestCase):
    def test_week(self):
        """result = task.Week("July 31, 2025")
        self.assertEqual(task.Week("July 31, 2025").print_week(), )""" # Don't want to test a print function

        test_day: datetime = datetime(2025, 7, 31)

        self.assertEqual(task.Week(test_day).daySentence, "It's July 31, 2025")
        self.assertEqual(task.Week(test_day).habits_this_week, [])



    def test_day(self):
        test_day: datetime = datetime(2025,7,31)
        self.assertEqual(task.Day(test_day).overlaps(task.Day(test_day)),True)