# Import necessary modules
from starlette.config import Config
from starlette.datastructures import Secret

try:
    config = Config(".env")  # Load configuration from .env file if exists
except FileNotFoundError:
    config = Config()  # Otherwise, create empty configuration object

# Get database connection strings from configuration
DB_URL = config.get("DB_CONNECTION_STR")
TEST_DB_URL = config.get("TEST_DB_URL")