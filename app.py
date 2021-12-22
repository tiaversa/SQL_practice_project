from sqlalchemy import *
from connction_db import *
from set_up import *

def main():
    # make the connection and add the database if necessary
    engine = engine_connect_db()
    # create the table and load information for queries into it.
    creating_the_setup(engine)
    return engine

main()