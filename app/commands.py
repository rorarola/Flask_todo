import click
from flask.cli imoprt with_appcontext

from app.routes import db
@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()