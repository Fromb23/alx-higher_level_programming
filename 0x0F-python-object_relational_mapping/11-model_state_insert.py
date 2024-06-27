#!/usr/bin/python3
"""
Script to add the State object “Louisiana” to the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_louisiana(username, password, dbname):
    """
    Adds the State object “Louisiana” to the database.
    """
    # Create an engine that stores data in my local mysql server
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}',
            pool_pre_ping=True
            )

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Bind the engine to the session
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Crate new state obj
    new_state = State(name="Louisiana")

    # Add the new obj to the session
    session.add(new_state)

    # Commit
    session.commit()

    # Print the new state's id
    print(new_state.id)

    # Close the session
    session.close()


if __name__ == '__main__':
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        add_louisiana(username, password, dbname)

