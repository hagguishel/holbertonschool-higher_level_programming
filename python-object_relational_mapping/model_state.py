#!/usr/bin/python3
"""
Import classes that inherit from Base
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    Class for State
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
