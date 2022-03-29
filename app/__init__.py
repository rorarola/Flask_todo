from flask import Flask
import os

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['SECRET_KEY'] = "FJKLSDJLFJELWFIE"

# uri = os.getenv("DATABASE_URL")
# if uri.startswith("postgres://"):
#     uri = uri.replace("postgres://", "postgresql://", 1)

SQLALCHEMY_DATABASE_URI = uri or 'sqlite:///tasks.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://cttpuforyugeim:734bb417f06bb58806341bd202501fc2d7886c6a76ab4d2321ec078653337a0e@ec2-3-229-161-70.compute-1.amazonaws.com:5432/d1e0ddo7njccdn'

from app import routes