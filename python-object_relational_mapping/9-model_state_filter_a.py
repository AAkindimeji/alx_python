from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

# Global variables for the MySQL connection
host = "127.0.0.1"
port = 3306
username = "learnakins"
password = "Akins@1234"
database_name = "hbtn_0e_6_usa"  # Updated database name

def list_states_with_a(username, password, database_name):
    """
    List all states in the database that contain the letter 'a'
    """
    # Create engine
    engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@localhost:3306/{database_name}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states containing the letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print states
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: script.py <mysql_username> <mysql_password> <database_name>")
