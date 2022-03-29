from flask import Flask
import os

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['SECRET_KEY'] = "FJKLSDJLFJELWFIE"

uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

SQLALCHEMY_DATABASE_URI = uri or 'sqlite:///tasks.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

from app import routes