#!/usr/bin/python3
"""Start link class to table in the database."""

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    """State class that represents the 'states' table."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Create an engine to connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create the 'states' table
    Base.metadata.create_all(engine)

    # Optionally, you can create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Example: Insert a new state into the 'states' table
    new_state = State(name='New State')
    session.add(new_state)
    session.commit()

    # Close the session when you're done
    session.close()
