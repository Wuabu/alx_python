"""State Class Documentation

The `State` class represents a state entity and corresponds to the 'states' table in a MySQL database.

Attributes:
    id (int): An auto-generated, unique integer representing the primary key of the state. It cannot be null.
    name (str): A string representing the name of the state with a maximum length of 128 characters. It cannot be null.

Example Usage:
    # Import necessary modules and classes
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from your_module_name import Base, State  # Replace 'your_module_name' with the actual module name

    # Connect to the MySQL server
    engine = create_engine('mysql://your_username:your_password@localhost:3306/your_database_name')

    # Bind the engine to the Base class
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object
    new_state = State(name='New State')

    # Add the state to the session and commit changes to the database
    session.add(new_state)
    session.commit()

    # Query and print all states from the 'states' table
    states = session.query(State).all()
    for state in states:
        print(f"State ID: {state.id}, Name: {state.name}")

    # Close the session
    session.close()
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """State Class

    Represents a state entity in the 'states' table of a MySQL database.

    Attributes:
        id (int): An auto-generated, unique integer representing the primary key of the state. It cannot be null.
        name (str): A string representing the name of the state with a maximum length of 128 characters. It cannot be null.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
