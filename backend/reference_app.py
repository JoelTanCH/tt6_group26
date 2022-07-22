from flask import Flask, redirect, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from random import choices
from datetime import datetime
import string
from config import DB_DELETION_THRESHOLD, NUM_COMBINATIONS

app = Flask(__name__)
app.config.from_pyfile(filename='config.py')
db = SQLAlchemy(app)
CORS(app)

class URLs(db.Model):
    '''
    "id" is an integer and will be used as the primary key 
    "created_at" is the UTC timing the original_url is stored in db 
    "original_url" is the text input typed out in the frontend 
    "shortened_url" is a 6 letter/number combination given to every unique original_url input 
    '''
    id = db.Column(db.Integer, primary_key = True)
    created_at = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    original_url = db.Column(db.String(512), nullable = False) #512 to accomodte very long url 
    shortened_url = db.Column(db.String(6), unique = True, nullable = False) 

    def __init__(self, original_url):
        self.original_url = original_url
        self.shortened_url = self.create_shortened_url()
 
    def create_shortened_url(self):
        '''
        function to create a shortened url made of 6 randomly chosen strings and numbers, chosen with replacement.
        refer to assumption 3 in README.md for the reason why k = 6 was chosen
        '''
        characters = string.ascii_letters + string.digits
        #random combination of 6 diff choices 
        shortened_url = ''.join(choices(population = characters, k=6))

        found_url = URLs.query.filter_by(shortened_url=shortened_url).first()

        #if found, generate the shortened url again
        if found_url:
            self.create_shortened_url()
        
        return shortened_url

    def reset_table(self, threshold = DB_DELETION_THRESHOLD) -> None:
        '''
        function to delete all records in table, triggered when db rows count 90% of 99.8mil as only 10% chance of 
        generating unique shortened url
        '''
        num_rows = URLs.query.count()
        #if num_rows in db crosses threshold 
        if(num_rows / NUM_COMBINATIONS >= threshold):
            print("ALERT: CLEARING ALL DATA FROM DATABASE")
            URLs.query.delete()
            db.session.commit()

def format_url(original_url):
    '''
    this function formats the original_url input by removing front and back whitespaces and ensures 'https://' is in the front. 
    This only circumvents some likely incorrect url naming conventions, not all 
    '''
    original_url = original_url.strip()
    potential_transfer_protocols = ['https://www.', 'https://', 'https:']

    for transfer_protocol in potential_transfer_protocols:
        if(original_url.startswith(transfer_protocol)):
            return original_url

    if(original_url.startswith('www.')):
        return potential_transfer_protocols[1] + original_url
    else:
        return transfer_protocol + original_url

#main function to shorten the original URL given
@app.route('/add_url', methods = ['POST'])
def add_url():
    '''
    if unique original url given, creates a 'URLs' object to be stored in db. shortened url is returned
    else, finds the already stored shortened url and returns it
    '''
    original_url = request.json['original_url']
    #format url 
    original_url = format_url(original_url=original_url)
    #check db to see if orignial url has been entered before
    found_url = URLs.query.filter_by(original_url=original_url).first()
    #if original url already exists 
    if found_url:
        return f"{found_url.shortened_url}"
    #if original url doesnt exist
    else:
        #create a new URL_Store object 
        url = URLs(original_url=original_url)
        #reset table if table has too many rows 
        url.reset_table()
        #add a new row to the database
        db.session.add(url)
        db.session.commit()
        return url.shortened_url

@app.route('/')
def hello():
    return "hello"

@app.route('/<short_url>')
def redirection(short_url):
    '''
    given a unique shortened url, the corresponding original url is retrieved. 
    the shortened url endpoint redirects to the original url. 
    '''
    original_url = URLs.query.filter_by(shortened_url=short_url).first()
    return redirect(original_url.original_url)

@app.errorhandler(404)
def page_not_found(e):
    return 'Backend is down!!!!!!!!',404

if __name__ == '__main__':
    app.run()
