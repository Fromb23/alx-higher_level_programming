#!/usr/bin/python3
"""
    Script to list all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, database):
    # Creating engine
    engine = create_engine((f'mysql+mysqldb://{username} '
                            ':{password}@localhost:3306/{database}'))

    # Creating session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying all State objects sorted by id
    states = session.query(State).order_by(State.id).all()

    # Displaying results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Closing session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    # Retrieving command-line arguments
    username, password, database = sys.argv[1:]

    # Calling function to list states
    list_states(username, password, database)
