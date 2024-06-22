#!/usr/bin/python3
"""
This script defines a State class and creates an
instance of Base using SQLAlchemy.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Instance of the Base class
Base = declarative_base()


class State(Base):
    """
    State class that links to the MySQL table 'states'.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
