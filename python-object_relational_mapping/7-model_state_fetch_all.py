from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

# Global variables for the MySQL connection
host = "127.0.0.1"
port = 3306
username = "learnakins"
password = "Akins@1234"
database_name = "hbtn_0e_0_usa"

def list_states():
    """
    List all states in the database
    """
    # Create engine
    engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database_name}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states
    states = session.query(State).order_by(State.id).all()

    # Print states
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()

if __name__ == "__main__":
    list_states()
