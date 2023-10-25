#!/usr/bin/python3
"""Print the first State object from the database hbtn_0e_6_usa."""
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

    # Query and print the first State object
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close the session when you're done
    session.close()
