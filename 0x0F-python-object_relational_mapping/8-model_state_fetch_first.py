#!/usr/bin/python3
"""
Script to print the first State object from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_first_state(username, password, dbname):
    """
    Prints the first State object from the specified database.
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

    # Query the database to retrieve the first State object ordered by id
    first_state = session.query(State).order_by(State.id).first()

    # Display the result
    if first_state:
        print(f'{first_state.id}: {first_state.name}')
    else:
        print("Nothing")

    # Close the session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        print_first_state(username, password, dbname)
