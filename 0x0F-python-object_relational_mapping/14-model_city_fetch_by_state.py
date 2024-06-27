#!/usr/bin/python3
"""
Script to list all City objects from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]

    # Create an engine
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}',
            pool_pre_ping=True
            )

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Bind the engien to the session
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # query all cities
    cities = (
            session.query(State, City.id, City)
            .filter(City.state_id == State.id).order_by(City.id).all()
            )

    # Print the cities
    for city in cities:
        print(f'{city.State.name}: ({city.id}) {city.State.name}')

    # Close session
    session.close()
