#!/usr/bin/python3
"""
Script to list all State objects that contain the
letter 'a' from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from model_state import Base, State


def list_states_with_a(username, password, dbname):
    """
    Lists all State objects containing the letter 'a'
    from the specified database.
    """
    # Create an engine that stores data
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}',
            pool_pre_ping=True
            )

    # Create all tables in the engine (if they don't exist)
    Base.metadata.create_all(engine)

    # Bind the engine to the session
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the database to retrieve all State objects
    states = session.query(State).filter(
            State.name.like('%a%')
            ).order_by(State.id).all()

    # Display the results
    for state in states:
        print(f'{state.id}: {state.name}')

    # Close the session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        list_states_with_a(username, password, dbname)
