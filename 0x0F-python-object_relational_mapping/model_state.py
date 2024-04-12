#!/usr/bin/python3
"""Model for the State table in the database."""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class State(Base):

    """
    Represents a state in the database
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)


# create engine
engine = create_engine('mysql://root:root@localhost/hbtn_0e_6_usa')

# Create all tables
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)

# Create a session obj
session = Session()

# Query all db using session
state = session.query(State).all()
