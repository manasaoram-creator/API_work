from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv

# Load environment variables from a .env file.
# This will search for the .env file in the current directory and parent directories.
load_dotenv()

# Load credentials from environment variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_TNS_NAME = os.getenv("DB_TNS_NAME")

# Validate that the environment variables were loaded correctly
if not all([DB_USER, DB_PASSWORD, DB_TNS_NAME]):
    raise ValueError("Database credentials not found. Please ensure a .env file exists in the project root and contains DB_USER, DB_PASSWORD, and DB_TNS_NAME.")

# Depending on how we're connecting to the DB, we will need to use one of the below
# It's best practice to build the URL from environment variables for security.
TNS_URL_TEMPLATE = "oracle+oracledb://{user}:{password}@{tns_name}"

FINAL_URL = TNS_URL_TEMPLATE.format(user=DB_USER, password=DB_PASSWORD, tns_name=DB_TNS_NAME)

engine = create_engine(FINAL_URL)
metadata = MetaData()

def get_database():
    """Returns a session from the database engine."""
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
