from flask import Flask

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['SECRET_KEY'] = "FJKLSDJLFJELWFIE"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

from app import routes