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

def get_first_state():
    """Print the first State object from the database"""
    # Create engine using global connection variables
    engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database_name}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get the first state
    first_state = session.query(State).order_by(State.id).first()

    # Check if there is a state
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close session
    session.close()

if __name__ == "__main__":
    get_first_state()
