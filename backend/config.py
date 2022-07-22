import os
from dotenv import load_dotenv
load_dotenv('./.env')

## .env variables for MySQL 
HOST = os.environ.get("HOST")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
DB = os.environ.get("DB")

## keys for currency converter 
X_RapidAPI_Key = os.environ.get("X-RapidAPI-Key")
X_RapidAPI_Host = os.environ.get("X-RapidAPI-Host")

CURRENCY_CONVERTER_URL = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
AVAIL_CURRENCIES_URL = "https://currency-converter18.p.rapidapi.com/api/v1/supportedCurrencies"