from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class
Base = declarative_base()

class State(Base):
    __tablename__ = 'states'  # Links to MySQL table states

    # Define the columns
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# Connect to the MySQL database
# Note: Replace special characters in the password with URL encoded values
engine = create_engine('mysql+mysqlconnector://learnakins:Akins%40123@127.0.0.1:3306/hbtn_0e_6_usa')
Base.metadata.create_all(engine)  # Create the tables in the database

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Example: Add a new State
new_state = State(name='New State Name')
session.add(new_state)
session.commit()
