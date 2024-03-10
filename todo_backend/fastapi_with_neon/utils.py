from sqlmodel import create_engine
from dotenv import load_dotenv, find_dotenv
from os import getenv

connection_str: str = str(getenv("DB_CONNECTION_STR"))
engine = create_engine(connection_str, echo=True, pool_pre_ping=True)