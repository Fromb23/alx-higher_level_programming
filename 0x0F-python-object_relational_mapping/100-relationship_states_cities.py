#!/usr/bin/python3
"""
Script to create the State "California" with the City
"San Francisco" in a database using SQLAlchemy.
"""
import sys
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Create an engine
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}',
            pool_pre_ping=True
            )
    # Create table in the db
    Base.metadata.create_all(engine)

    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the state and city
    california = State(name='California')
    san_francisco = City(name='San Francisco', state=california)

    # add the obj to the session and commit
    session.add(california)
    session.add(san_francisco)
    session.commit()

    # Close the session
    session.close()
