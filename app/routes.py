from app import app
from flask import render_template, redirect, url_for

# database (之後看能不能找更好的地方放)
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

db = SQLAlchemy(app)

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary key => value have to be unique
    task_name = db.Column(db.String(200), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<name %r>' % self.task_name

# form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
class TaskForm(FlaskForm):
    task_name = StringField('task_name', validators=[DataRequired()])
    submit = SubmitField('+')




@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    task_name = None
    form = TaskForm()
    if form.validate_on_submit():
        # Hash the password!!!
        task = Tasks(task_name=form.task_name.data)
        db.session.add(task)
        db.session.commit()
        form.task_name.data = ''
    tasks = Tasks.query.order_by(Tasks.date_added)
    return render_template("index.html", 
        form=form,
        tasks=tasks)

@app.route('/delete_task/<id>')
def delete_task(id):
    task = Tasks.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))