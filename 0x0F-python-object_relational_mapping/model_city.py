#!/usr/bin/python3
"""
Script to define the City class which links to the MySQL table 'cities'.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class that represents the 'cities' table in the database.
    Attributes:
        id (int): The city's id.
        name (str): The city's name.
        state_id (int): The state id the city belongs to.
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
