#!/usr/bin/python3
"""Add the State object "Louisiana" to the database hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine to connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(mysql_username, mysql_password, database_name))

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object
    new_state = State(name='Louisiana')

    # Add the new State object to the session and commit it to the database
    session.add(new_state)
    session.commit()

    # Print the new states.id after creation
    print(new_state.id)

    # Close the session when you're done
    session.close()
