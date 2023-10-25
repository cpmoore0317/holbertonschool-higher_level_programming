#!/usr/bin/python3
"""Change the name of a State object in the database hbtn_0e_6_usa."""
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

    # Query and change the name of the State object where id is 2 to "New Mexico"
    state_to_update = session.query(State).filter(State.id == 2).first()

    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session when you're done
    session.close()
