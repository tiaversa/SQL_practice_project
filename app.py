from sqlalchemy import *
import pymysql


def engine_connect_db():
    engine = create_engine(
        f'mysql+pymysql://{mysql_db_config["user"]}:{mysql_db_config["password"]}@{mysql_db_config["host"]}'
    )  # connect to server

    # check if database exists if not add the database
    engine.execute(
        f"CREATE DATABASE IF NOT EXISTS {mysql_db_config['database']};"
    )  # create db

    # adding the database to the engine call
    engine = create_engine(
        f'mysql+pymysql://{mysql_db_config["user"]}:{mysql_db_config["password"]}@{mysql_db_config["host"]}/{mysql_db_config["database"]}'
    )
    return engine


mysql_db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '*Saltlake5',
    'port': 3306,
    'database' : 'linux_test'
}

engine = engine_connect_db()
print(engine)
print('hi')
