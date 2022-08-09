from functools import wraps
from flask import Flask, make_response, render_template, request, jsonify, json, redirect
from flask_cors import CORS
import mysql.connector as mysql
from mysql.connector import Error
import yaml
from datetime import date, datetime, timedelta
import jwt
from functools import wraps
import requests, json

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRETY_KEY'] = 'thisistechtrek6'
CORS(app)

try:
    db = yaml.load(open('db.yaml'), Loader=yaml.Loader)
    connection  = mysql.connect(
                host=db['mysql_host'],
                user=db['mysql_user'],
                passwd=db['mysql_password'],
                db=db['mysql_db'])
    
    def token_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            print(request.args)
            token = request.args.get('token') # http://127.0.0.1:500/route?token=
            print(token)
            if not token:
                return jsonify({'message': 'token is missing'}), 403

            try:
                data = jwt.decode(token, app.config['SECRETY_KEY'], algorithms=["HS256"])
                print('data: {}'.format(data))
            except:
                return jsonify({'message':'Token is invalid'}), 403
            
            return f(*args, **kwargs)
        
        return decorated

    def getUserPassword(userName):
        try:
            statement = "select * from user where username = '{}'".format(userName)
            cur = connection .cursor()
            cur.execute(statement)
            password = cur.fetchall()
            password = password[0][2]
            cur.close()
            return password
        except:
            return None

    class create_dict(dict): 
    
        # __init__ function 
        def __init__(self): 
            self = dict() 
            
        # Function to add key:value 
        def add(self, key, value): 
            self[key] = value
           
           
    def getAllUsers(json_str=True):
        cur = connection.cursor()
        cur.execute("SELECT * FROM user")
        userDetails = cur.fetchall()
        cur.close()
        mydict = create_dict()
        for row in userDetails:
            mydict.add(row[0],({"username":row[1],"user":row[3]}))
        return  json.dumps(mydict, indent=2, sort_keys=True)


    @app.route('/users')
    # @token_required
    def users():
        userDetails = getAllUsers()
        if userDetails:
            return userDetails
        
        
    @app.route('/login', methods=['POST'])
    def login():
        auth = request.authorization
        userInput = auth.username
        passwordInput = auth.password
        passwordDB = getUserPassword(userInput) 
        if(userInput and passwordInput == passwordDB):
            token = jwt.encode({'user' : auth.username, 'exp': datetime.utcnow() + timedelta(minutes=120)}, app.config['SECRETY_KEY'] )
            return jsonify({'token': token})
        return make_response('could not verify!', 404, {'WWW-Authenticate': 'Basic realm:"login required"'})
    
    @app.route('/get_currencies_available', methods = ['GET'])
    def get_all_currencies():
        '''
        :input: none
        :output: List of Json strings 
                [{"symbol":"USD","name":"United States Dollar"},
                {"symbol":"ALL","name":"Albania Lek"}, ....]
        '''

        headers = {
            "X-RapidAPI-Key": db['X-RapidAPI-Key'],
            "X-RapidAPI-Host": db['X-RapidAPI-Host']
        }
        response = requests.request("GET", db['AVAIL_CURRENCIES_URL'], headers=headers)
        json_data = json.loads(response.text)
        currency_symbols = [currency['symbol'] for currency in json_data]

        return {'currency_symbols': currency_symbols}

    @app.route('/currency_convert', methods = ['GET','POST'])
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
        print(request)
        print(request.json)
        convert_from = request.json['convert_from']
        convert_to = request.json['convert_to']
        convert_amount = request.json['convert_amount']

        print(convert_from, convert_to, convert_amount)
        print('hello')

        querystring = {"from" : convert_from,
                        "to" : convert_to,
                        "amount" : convert_amount}

        headers = {
            "X-RapidAPI-Key": db['X-RapidAPI-Key'],
            "X-RapidAPI-Host": db['X-RapidAPI-Host']
        }

        response = requests.request("GET", db['CURRENCY_CONVERTER_URL'], headers=headers, params=querystring)

        return response.text
    
    
    if __name__ == "__main__":
        app.run()
        
except Error as e:
    print("Error while connection to Mysql", e)
finally:
    connection.close()
    print("==== mysql closed===")