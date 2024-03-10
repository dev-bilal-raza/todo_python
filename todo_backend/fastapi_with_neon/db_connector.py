from sqlmodel import SQLModel
from .utils import engine

def db_connector():
    SQLModel.metadata.create_all(engine)
    
if __name__ == '__main__':
    db_connector()      