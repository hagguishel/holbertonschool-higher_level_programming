#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
from model_city import City

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

    Session = sessionmaker(bind=engine)
    session = Session()

    results = (
        session.query(State.name, City.id, City.name)
        .join(City)
        .order_by(City.id)
        .all()
    )

    for state_name, city_id, city_name in results:
        print(f"{state_name}: ({city_id}) {city_name}")

    session.close()
