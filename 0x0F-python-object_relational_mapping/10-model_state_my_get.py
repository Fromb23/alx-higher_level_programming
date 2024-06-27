#!/usr/bin/python3
"""
Script to print the State object with the name
passed as argument from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from model_state import Base, State


def list_state_by_name(username, password, dbname, state_name):
    """
    Prints the sate obj wit the specified name from the db
    """
    # Create an engine that stores data in the local mysql server
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}',
            pool_pre_ping=True
            )

    # Create all tables in the engine (if any doesn't exist)
    Base.metadata.create_all(engine)

    # Bind the engine to the session
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the db to retrive the State obj with the specified haje
    state = session.query(State).filter(State.name == state_name).first()

    # Display the result
    if state:
        print(f'{state.id}')
    else:
        print("Not found")

    # Close the session
    session.close()

    if __name__ == '__main__':
        if len(sys.argv) == 5:
            username = sys.argv[1]
            password = sys.argv[2]
            dbname = sys.argv[3]
            state_name = sys.argv[4]
            list_state_by_name(username, password, dbname, state_name)
