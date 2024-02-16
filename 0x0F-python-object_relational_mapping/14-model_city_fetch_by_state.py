#!/usr/bin/python3
"""Script that prints all City objects from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():
    """Main function to fetch and print City objects"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state_name = session.query(
            State).filter_by(id=city.state_id).first().name
        print("{}: ({}) {}".format(state_name, city.id, city.name))

    session.close()


if __name__ == "__main__":
    main()
