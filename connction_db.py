from sqlalchemy import *
import pymysql

def db_config():
    local_server = {
        'host': 'localhost',
        'user': 'root',
        'password': '*Saltlake5',
        'port': 3306,
        'database' : 'linux_test'
    }
    docker_server = {
        'host': 'mysql_db',
        'user': 'ti',
        'password': 'secret',
        'port': 3307,
        'database' : 'linux_test'
    }
    mysql_db_config = local_server
    #mysql_db_config = docker_server
    return mysql_db_config

    
def engine_connect_db():
    mysql_db_config = db_config()
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