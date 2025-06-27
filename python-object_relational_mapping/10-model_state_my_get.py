#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == "__main__":
    """
    Connects to the database and lists all State objects,
    sorted by id in ascending order.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    search_name = sys.argv[4]
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == search_name).first()
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
