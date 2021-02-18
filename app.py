from weather_api import Weather
import dateutil.parser
import hashlib 
import os
import sys
from flask import Flask, request, json, render_template

app = Flask(__name__)

@app.route('/')
def main_route():
    return 'Weather API'

@app.route('/forecasts/v1/daily/1day/', methods=['GET'])
def get_1_day_forcast():

    if request.method == 'GET':
        # check authentication
        user_key = request.args.get('key', '')
        auth = simple_authentication(user_key)
        
        if auth == 1:
            city = request.args.get('city', '')

            w = Weather(city)

            the_key = w.get_city_key()

            response = app.response_class(
                response=w.get_one_day_forcast(the_key),
                status=200,
                mimetype='application/json'
            )

            return response

    return "nothing here"

    

@app.route('/forecasts/v1/daily/5day/', methods=['GET'])
def get_5_day_forcast():


    if request.method == 'GET':

        # check authentication
        user_key = request.args.get('key', '')
        auth = simple_authentication(user_key)
        
        if auth == 1:

            city = request.args.get('city', '')

            w = Weather(city)

            the_key = w.get_city_key()

            response = app.response_class(
                response=w.get_five_day_forcast(the_key),
                status=200,
                mimetype='application/json'
            )

            return response

    return "nothing here"



@app.route('/forecasts/v1/daily/5day/barchart/', methods=['GET'])
def get_5_day_forcast_barchart():

    if request.method == 'GET':
        city = request.args.get('city', '')

        w = Weather(city)

        the_key = w.get_city_key()

        response = w.get_five_day_forcast(the_key)
        
        resp = json.loads(response)

        dates = []
        temps = []
        for d in resp['Forcasts']:

            dates.append(d['Date'])
            temps.append(d['Max'])


        print(temps)
        return render_template('barchart.html', dates=dates, temps=temps)
        

    return "nothing here"


def simple_authentication(user_key):

    USER_API_KEY = os.environ.get("USER_API_KEY")
    SALT = os.environ.get("SALT")

    encoded_key = USER_API_KEY + SALT

    result = hashlib.md5(encoded_key.encode()) 

   
    encryption = result.hexdigest()

    if encryption  == user_key:
        return 1

    return 0
