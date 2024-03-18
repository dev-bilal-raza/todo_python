# Import necessary modules
from .setting import DB_URL, TEST_DB_URL

# ========================= here I have saved a connection strings for original database and test database =======================
db_connction_str = str(DB_URL).replace("postgrsql", "postqresql+psycopg")
test_db_connction_str = str(TEST_DB_URL).replace("postgrsql", "postqresql+psycopg")
# ================================================================================================================================

# Define allowed origins for CORS middleware
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]