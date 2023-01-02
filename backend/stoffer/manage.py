import click
from flask.cli import with_appcontext


@click.command("init")
@with_appcontext
def init():
    """Create a new admin user"""
    from stoffer.extensions import db
    from stoffer.models import User

    click.echo("create user")
    user = User(username="admin", email="neil@ghose.us", password="admin123", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")
