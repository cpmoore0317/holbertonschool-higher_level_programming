#!/usr/bin/python3
"""Print all City objects from the database hbtn_0e_14_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import State

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

    # Query and list all City objects sorted by id with their respective State names
    cities = session.query(City).join(State).order_by(City.id).all()

    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    # Close the session when you're done
    session.close()
