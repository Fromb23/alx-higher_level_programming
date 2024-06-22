#!/usr/bin/python3
"""
Script to list all State objects from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def list_states(username, password, dbname):
    """
    Lists all State objects from the specified database.
    """

    # Create an engine that stores data in the local MySQL server
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

    # Query the database to retrieve all State objects sorted by id
    states = session.query(State).order_by(State.id).all()

    # Display the results
    for state in states:
        print(f'{state.id}: {state.name}')

    # Close session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        list_states(username, password, dbname)
