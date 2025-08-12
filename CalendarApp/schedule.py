from task import Task

class Schedule:
    def __init__(self):
        self.timeline = []
        self.task_list = []


    def remove_task(self, task: Task):
        if task in self.task_list:
            self.task_list.remove(task)