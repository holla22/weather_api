from weather_api import Weather
from flask import Flask, request, json, render_template
app = Flask(__name__)


# API KEY: GDs6YondZ1GmEdc1DZ6s8P4ny5wAW6qg
# Accuweather

@app.route('/')
def main_route():

    w = Weather('brackenfell')

    the_key = w.get_city_key()
    return 'Weather API'

@app.route('/forecasts/v1/daily/1day/', methods=['GET'])
def get_1_day_forcast():

    if request.method == 'GET':
        city = request.args.get('city', '')

        w = Weather(city)

        the_key = w.get_city_key()

        response = app.response_class(
            response=w.get_one_day_forcast(the_key),
            status=200,
            mimetype='application/json'
        )

        return response

    

@app.route('/forecasts/v1/daily/5day/', methods=['GET'])
def get_5_day_forcast():


    if request.method == 'GET':
        city = request.args.get('city', '')

        w = Weather(city)

        the_key = w.get_city_key()

        response = app.response_class(
            response=w.get_five_day_forcast(the_key),
            status=200,
            mimetype='application/json'
        )

        return response



@app.route('/forecasts/v1/daily/5day/barchart/', methods=['GET'])
def get_5_day_forcast_barchart():

    if request.method == 'GET':
        city = request.args.get('city', '')

        w = Weather(city)

        the_key = w.get_city_key()

        response = w.get_five_day_forcast(the_key)

        dates = []
        temps = []
        for d in response['Forcasts']:
            dates.append(d['Date'])
            temps.append(d['Max'])


        print(temps)
        return render_template('barchart.html', dates=dates, temps=temps)
        

    return "hello"


