#!/usr/bin/python3
"""Script to delete all State objects
with a name containing the letter 'a' from the database"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Main function to connect to MySQL and delete State objects"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(
        State).filter(State.name.like('%a%')).all()

    if states_to_delete:
        for state in states_to_delete:
            session.delete(state)
        session.commit()
        print("State objects with names containing 'a deleted successfully")
    else:
        print("No State objects with names containing 'a' found")

    session.close()


if __name__ == "__main__":
    main()
