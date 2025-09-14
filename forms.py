from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import DateField
from wtforms.validators import DataRequired, Length

class TaskInputForm(FlaskForm):
    task_name = StringField('Task Name', validators=[DataRequired(), Length(min=2, max=100)])
    description = StringField('Task Description', validators=[DataRequired(), Length(min=2, max=400)])
    start_time = DateField('Start Time', validators=[DataRequired()])
    duration = DateField('Duration', validators=[DataRequired()])