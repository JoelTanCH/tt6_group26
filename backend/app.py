from flask import Flask, redirect, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import HOST, USER, PASSWORD, DB, X_RapidAPI_Host, X_RapidAPI_Key, CURRENCY_CONVERTER_URL, AVAIL_CURRENCIES_URL
import pymysql, requests

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] =f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DB}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #ignore tracking changes to database
db = SQLAlchemy(app)


@app.route("/test_db", methods = ['POST'])
def test_connection():
        original_url = request.json['original_url']


@app.route('/')
def hello():
    return "hello"

@app.route('/get_currencies_available', methods = ['GET'])
def get_all_currencies():
    '''
    :input: none
    :output: List of Json strings 
            [{"symbol":"USD","name":"United States Dollar"},
            {"symbol":"ALL","name":"Albania Lek"}, ....]
    '''

    headers = {
        "X-RapidAPI-Key": X_RapidAPI_Key,
        "X-RapidAPI-Host": X_RapidAPI_Host 
    }
    response = requests.request("GET", AVAIL_CURRENCIES_URL, headers=headers)
    #print(response)
    return response.text

@app.route('/currency_convert', methods = ['GET'])
def convert_currency():
    '''
    converts the currency from any  to specified currency 

    :input: {
        "convert_from" : string 
        "convert_to" : string 
        "convert_amount" : float 
    }

    :output: {
        {
            "success":true,
            "validationMessage":[],
            "result":{
                "from":"AUD",
                "to":"CAD",
                "amountToConvert":4,
                "convertedAmount":3.5587579628824426
                }
            }
        }
    '''
    convert_from = request.json['convert_from']
    convert_to = request.json['convert_to']
    convert_amount = request.json['convert_amount']

    querystring = {"from" : convert_from,
                    "to" : convert_to,
                    "amount" : convert_amount}

    headers = {
        "X-RapidAPI-Key": X_RapidAPI_Key,
        "X-RapidAPI-Host": X_RapidAPI_Host 
    }

    response = requests.request("GET", CURRENCY_CONVERTER_URL, headers=headers, params=querystring)

    return response.text

if __name__ == '__main__':
    
    app.run()