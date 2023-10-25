#!/usr/bin/python3
"""Defines the city class."""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
from sqlalchemy.orm import relationship

class City(Base):
    """City class that represents the 'cities' table."""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Define a relationship to the State model
    state = relationship("State")
