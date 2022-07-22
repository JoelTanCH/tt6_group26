import os
from dotenv import load_dotenv

load_dotenv()

DB_USERNAME = os.environ.get("MYSQL_USERNAME")
DB_PASSWORD = os.environ.get("MYSQL_PASSWORD")
DB_NAME = "multicurrency"
# openssl rand -hex 32
ACCESS_SECRET_KEY = os.environ.get("ACCESS_SECRET_KEY")
REFRESH_SECRET_KEY = os.environ.get("REFRESH_SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 60

print(DB_USERNAME)