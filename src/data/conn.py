import os
import requests
import pandas as pd
from datetime import datetime
# from mysql.connector import Error
# import mysql.connector

from dotenv import load_dotenv


# load .env
load_dotenv()

# load API key
RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')

#print(RAPIDAPI_KEY)

# checking env connection is working
# print("Value of MY_VARIABLE:", RAPIDAPI_KEY)





# Set API request headers:

# set up API URL
url = 'https://seeking-alpha.p.rapidapi.com/symbols/get-historical-prices'

querystring = {
    "symbol":"nvda",
    "start":"2000-02-02",
    "end":"2022-02-02",
    "show_by":"week",
    "sort":"as_of_date"
  }

headers = {
        'X-RapidAPI-Key': RAPIDAPI_KEY,
        'X-RapidAPI-Host': 'seeking-alpha.p.rapidapi.com'
  }


def get_historical_data (url, headers, querystring):
        try:
                response = requests.get(url, headers=headers, params=querystring)
                response.raise_for_status()
                return response.json()
        
        except requests.exceptions.HTTPError as http_error_message:
                print(f"[HTTP ERROR]: {http_error_message}")
        
        except requests.exceptions.ConnectionError as connect_error_message:
                print(f"[CONNECTION ERROR]: {connect_error_message}")
        
        except requests.exceptions.Timeout as timeout_error_message:
                print(f"[TIMOUT ERROR]: {timeout_error_message}")
                
        except requests.exceptions.RequestException as other_error_message:
                print(f"[UNKNOWN ERROR]: {other_error_message}")
                



# checking function resposne 



