#!/usr/bin/python3
"""Script to change the name of a State object from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Main function to connect to MySQL and chnage Staet object's name"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}: {}@localhose:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()

    if state:
        state.name = 'New Mexico'
        session.commit()
        print("Name changed successfully")
    else:
        print("State with id 2 not found")

    session.close()


if __name__ == "__main__":
    main()
