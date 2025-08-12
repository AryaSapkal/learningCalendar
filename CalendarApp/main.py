import task
from taskManager import TaskManager
import datetime

def main():
    task_manager = TaskManager()

    a_starting_time = datetime.datetime.now()
    some_day = task.Day(a_starting_time)
    some_duration = datetime.timedelta(hours=2)

    some_task = task.Task(a_starting_time, some_duration, "A Random Task", "Some random description.")

    task_manager.add_task(some_day, some_task)


    print(task_manager.tasks)













if __name__ == '__main__':
    main()




"""



a_starting_time = datetime.datetime(2025, 7, 31)

my_week = Week("July 31, 2025")
my_week.print_week()
print(my_week.daySentence)
print(my_week.habit)

my_week.habit = ["Sleep 30 minutes earlier each night."]
print(my_week.habit)



"""