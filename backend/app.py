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