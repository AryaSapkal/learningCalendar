from __future__ import annotations
import datetime
from typing import List
from pathlib import Path


class TimeBlock:
    """Creates a time block given a starting time and duration"""
    def __init__(self, time_start: datetime.datetime, duration: datetime.timedelta):
        self.time_start: datetime.datetime = time_start
        self.duration = duration

    @property
    def time_end(self):
        return self.time_start + self.duration

    def overlaps(self, other: TimeBlock):
        return not (self.time_end <= other.time_start)


class Week(TimeBlock):

    def __init__(self, week_start: datetime.datetime):  # Assumes that string_date is only a date that is a Sunday
        super().__init__(time_start=week_start, duration=datetime.timedelta(weeks=1))
        self.week_start: datetime.datetime = week_start
        self.week_start_string: str = datetime.datetime.strftime(self.week_start, format="%B %d, %Y")
        self.habits_this_week: list = []

    def print_week(self):
        for i in range(7):
            print(self.week_start.strftime('%A, %B %d, %Y'))
            self.week_start = self.week_start + datetime.timedelta(days=1)

    @property
    def the_week(self):
        result = ""
        for i in range(7):
            result += self.week_start.strftime('%A, %B %d, %Y')
            self.week_start = self.week_start + datetime.timedelta(days=1)

        return result

    @property
    def daySentence(self):
        return f"It's {self.week_start.strftime('%B %d, %Y')}"

    @property
    def habit(self):
        return self.habits_this_week

    @habit.setter
    def habit(self, habits: list[str]):
        self.habits_this_week = habits


class Day(TimeBlock):
    """A Day starts from an exact time and ends one day after"""
    def __init__(self, time_start: datetime.datetime):
        super().__init__(duration=datetime.timedelta(days=1), time_start=time_start)
        self.task_list: list[str] = []

    @property
    def dayName(self):
        return datetime.datetime.strftime(self.time_start, "%A")

    @property
    def dayEnd(self):
        return self.time_start + self.duration


class Task(TimeBlock):
    def __init__(self, time_start: datetime.datetime, duration: datetime.timedelta, title: str | None = None, description: str | None = None, complete: bool = False, priority: int | None = None):
        super().__init__(time_start, duration)
        self.title = title
        self.description = description
        self.complete = complete
        self.priority = priority
        self.__db_id = None

    @property
    def name(self):
        return f"Time: {self.time_start.strftime('%A, %B %d, %Y %I:%M %p')}\tDuration: {self.duration}\tTask Name: {self.title}"



    @property
    def task_dict(self):
        return {
            "time_start": self.time_start,
            "duration": self.duration,
            "title": self.duration,
            "description": self.description,
            "complete": self.complete,
            "priority": self.priority
        }











