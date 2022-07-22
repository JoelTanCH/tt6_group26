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
            userRecord = cur.fetchall()
            password = userRecord[0][2]
            userId = userRecord[0][0]
            cur.close()
            return userId, password
        except:
            return None, None

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
    
    def getAllWallets(json_str=True):
        cur = connection.cursor()
        cur.execute("SELECT * FROM wallet")
        walletDetails = cur.fetchall()
        cur.close()
        mydict = create_dict()
        for row in walletDetails:
            mydict.add(row[0],({"user_id":row[1], "name":row[2]}))
        return  json.dumps(mydict, indent=2, sort_keys=True)
    
    def getAllWalletsByUserId(userId, json_str=True):
        cur = connection.cursor()
        statement = "SELECT * FROM wallet where user_id={}".format(userId)
        print(statement)
        cur.execute(statement)
        walletDetails = cur.fetchall()
        cur.close()
        mydict = create_dict()
        for row in walletDetails:
            mydict.add(row[0],({"name":row[2]}))
        return  json.dumps(mydict, indent=2, sort_keys=True)
    
    def getAllExchangeRates(json_str=True):
        cur = connection.cursor()
        cur.execute("SELECT * FROM exchange_rate")
        exchangeRateDetails = cur.fetchall()
        cur.close()
        mydict = create_dict()
        for row in exchangeRateDetails:
            mydict.add(row[0],({"base_currency":row[1],"exchange_currency":row[2], "rate":row[3]}))
        return  json.dumps(mydict, indent=2, sort_keys=True)


    @app.route('/users')
    @token_required
    def users():
        userDetails = getAllUsers()
        if userDetails:
            return userDetails
        
    @app.route('/wallets/<int:userId>')
    def walletsByUserId(userId):
        walletDetails = getAllWalletsByUserId(userId)
        if walletDetails:
            return walletDetails
        
    @app.route('/wallets')
    def wallets():
        walletDetails = getAllWallets()
        if walletDetails:
            return walletDetails
        
    @app.route('/exchanges')
    def exchangeRates():
        exchangeRateDetails = getAllExchangeRates()
        if exchangeRateDetails:
            return exchangeRateDetails
        
    # @app.route('/currency')
    # def exchangeRate():
    #     exchangeRateDetails = getAllExchangeRate()
    #     if exchangeRateDetails:
    #         return exchangeRateDetails
        
        
    @app.route('/login', methods=['POST'])
    def login():
        auth = request.authorization
        userInput = auth.username
        passwordInput = auth.password
        userIdDB, passwordDB = getUserPassword(userInput) 
        if(userInput and passwordInput == passwordDB):
            token = jwt.encode({'user' : auth.username, 'userId': userIdDB,'exp': datetime.utcnow() + timedelta(minutes=120)}, app.config['SECRETY_KEY'] )
            return jsonify({'token': token})
        return make_response('could not verify!', 404, {'WWW-Authenticate': 'Basic realm:"login required"'})
    
        
    if __name__ == "__main__":
        app.run()
        
except Error as e:
    print("Error while connection to Mysql", e)
finally:
    connection.close()
    print("==== mysql closed===")