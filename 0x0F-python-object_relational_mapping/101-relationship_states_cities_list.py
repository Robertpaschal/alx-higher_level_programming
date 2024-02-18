#!/usr/bin/python3
"""Script that lists all State Objects and corresponding City obkects contained
in the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State


def main():
    """Main function to list state and corresponding City objects"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(
            state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()


if __name__ == "__main__":
    main()
