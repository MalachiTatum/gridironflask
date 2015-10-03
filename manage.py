from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

from app import app, db

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def resetdb():
    dbHost = current_app.config.get('DB_HOST')
    engine = create_engine('postgresql+psycopg2://postgres:@' + dbHost + ':5432/template1')
    session = sessionmaker(bind=engine)()
    session.connection().connection.set_isolation_level(0)
    #session.execute('DROP DATABASE IF EXISTS gridironflaskdb')
    session.execute('CREATE DATABASE gridironflaskdb')
    session.connection().connection.set_isolation_level(1)

@manager.command
def resetdb():
    engine = create_engine('postgresql+psycopg2://postgres:@127.0.0.1:5432/template1')
    session = sessionmaker(bind=engine)()
    session.connection().connection.set_isolation_level(0)
    session.execute('DROP DATABASE IF EXISTS gridironflaskdb')
    session.execute('CREATE DATABASE gridironflaskdb')
    session.connection().connection.set_isolation_level(1)

if __name__ == '__main__':
    manager.run()
