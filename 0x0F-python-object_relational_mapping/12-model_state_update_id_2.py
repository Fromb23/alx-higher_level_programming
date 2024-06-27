#!/usr/bin/python3
"""
Script to change the name of the State object with id 2
to “New Mexico” in the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def change_obj_name(username, password, dbname):
    """
    Changes the name of the State object with id 2 to 'New Mexico'.
    """
    # Create an engine
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}',
            pool_pre_ping=True
            )

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Bind the engine to the sessioon
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # query
    session.query(State).filter(State.id == 2).update(
            {State.name: 'New Mexico'}, synchronize_session=False)

    # Commit
    session.commit()

    # Close session
    session.close()


if __name__ == '__main__':
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        change_obj_name(username, password, dbname)
