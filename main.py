from task import Task
from taskManager import TaskManager
import datetime
import sqlite3
from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')



"""def main():
    my_task_manager = TaskManager()

    my_task = Task(datetime.datetime(2025, 8, 27), datetime.timedelta(hours=2), "Do the laundry", complete=False)
    #my_schedule = Schedule()
    my_task_manager.schedule.create_task(my_task)

    conn = sqlite3.connect('tasks.db', isolation_level=None)
    c = conn.cursor()
    with conn:
        c.execute(f"SELECT * FROM tasks WHERE id={my_task.db_id}")
        #print(f'Here they are:{c.fetchall()}')"""


tasks = [
    {
        'id': '4',
        'task_name': 'Study for the intro to chem quiz on Friday.',
        'description': 'Study nomenclature, isotopes, dim analysis, and the basics.',
        'start_time': str(datetime.datetime.now()),
        'duration': datetime.timedelta(hours=2)
    },
    {
        'id': '5',
        'task_name': 'Work on the Battleship project.',
        'description': 'Work on the 1st part of the project. Leave enough time to ask questions.',
        'start_time': str(datetime.datetime.now()),
        'duration': datetime.timedelta(hours=2)
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", tasks=tasks)






if __name__ == '__main__':
    #main()
    app.run(debug=True)




