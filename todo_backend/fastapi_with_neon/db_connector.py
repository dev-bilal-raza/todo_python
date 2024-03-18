# Import necessary modules
from sqlmodel import SQLModel, Session
from .const import DB_URL, TEST_DB_URL
from sqlmodel import create_engine
from sqlmodel.pool import StaticPool

# Creating engine for connecting to the main database
db_engine = create_engine(DB_URL, connect_args={
    "sslmode": "require"}, pool_recycle=300)

# Creating engine for connecting to the test database
testdb_engine = create_engine(TEST_DB_URL,connect_args={
    "sslmode": "require"}, poolclass=StaticPool)

# Function to initialize database tables for the main database
def db_connector():
    SQLModel.metadata.create_all(db_engine)

# Function to initialize database tables for the test database
def testdb_connector():
    SQLModel.metadata.create_all(testdb_engine)

# Function to get a session from the main database
def get_session():
    with Session(db_engine) as session:
        yield session
