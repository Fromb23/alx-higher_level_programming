#!/usr/bin/python3
"""Model for the State table in the database."""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create Base instance
Base = declarative_base()


class State(Base):
    """
    Represents a state in the database
    """
    __tablename__ = 'states'

    # Define columns
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


# Create engine
engine = create_engine(('mysql+mysqldb://root:root '
                        '@localhost:3306/hbtn_0e_6_usa?charset=latin1'))

# Create all tables
Base.metadata.create_all(engine)
