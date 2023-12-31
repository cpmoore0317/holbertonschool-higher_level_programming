#!/usr/bin/python3
"""List all State objects containing the letter 'a' from the database hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main":
    # Create an engine to connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and list all State objects containing the letter 'a' and sorted by id
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session when you're done
    session.close()
