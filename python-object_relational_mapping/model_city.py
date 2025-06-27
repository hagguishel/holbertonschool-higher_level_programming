#!/usr/bin/python3
"""
Import classes that inherit from Base
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    Class for City
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
