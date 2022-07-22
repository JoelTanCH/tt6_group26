from functools import wraps
from flask import Flask, make_response, render_template, request, jsonify, json, redirect
import mysql.connector as mysql
from mysql.connector import Error
import yaml
from datetime import date, datetime, timedelta
import jwt
from functools import wraps


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRETY_KEY'] = 'thisistechtrek6'

try:
    db = yaml.load(open('db.yaml'), Loader=yaml.Loader)
    connection  = mysql.connect(
                host=db['mysql_host'],
                user=db['mysql_user'],
                passwd=db['mysql_password'],
                db=db['mysql_db'])

    class create_dict(dict): 
    
        # __init__ function 
        def __init__(self): 
            self = dict() 
            
        # Function to add key:value 
        def add(self, key, value): 
            self[key] = value
           
           
    def getAllUsers(json_str=True):
        cur = connection .cursor()
        cur = connection .cursor()
        cur.execute("SELECT * FROM user")
        userDetails = cur.fetchall()
        cur.close()
        mydict = create_dict()
        for row in userDetails:
            mydict.add(row[0],({"username":row[1],"user":row[3]}))
        return  json.dumps(mydict, indent=2, sort_keys=True)

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

    @app.route('/users')
    # @token_required
    def users():
        userDetails = getAllUsers()
        print(type(userDetails))
        print(userDetails)
        if userDetails:
            return userDetails
        
    if __name__ == "__main__":
        app.run()
        
except Error as e:
    print("Error while connection to Mysql", e)
finally:
    connection.close()
    print("==== mysql closed===")

