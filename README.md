# Weather API wrapper

## About this project

This was written in flask, it's a simple API wrapper project. PS: remember to pip install the requirements.txt file.

The main code for the wrapper I have written in a Class inside weather_api.py all avg, max, min, mean, and median calculations is done on the 5 day forcast section only.

## Getting Started

> Clone this repo

> Register for an Accuweather API key here: https://developer.accuweather.com/

- first create a .env file for your API keys and secret stuff in the same repository folder 

> add the following sections to the .env file, replace {Accuweather API KEY HERE} with your own accuweather API key. 
> These are just temp keys and for demonstration purpose only.

- API_KEY={Accuweather API KEY HERE}
- USER_API_KEY=HEalKYLasbudgENtErTElaCRUlTHY
- SALT=RAfTYLIThIckLeWIsTEmICItAChag

> If you are on a mac or linux environment then there is a shell script "get_up_and_running.sh" which you can run to get this project running on a local web server.

> Else you would need run the following in your terminal to get the web server up.

`export FLASK_APP=app.py`
`export FLASK_ENV=development`
`flask run`


- User API key for testing purpose only - d2e78bbf822ca098393d50423eae7f6a

## Running the endpoints to see results

- I have a folder with a postman JSON export, which you can import into your own postman and trigger the endpoints
- or just use the curl commands below in your terminal

- 1 day weather results
`curl --location --request GET 'http://127.0.0.1:5000/forecasts/v1/daily/1day/?key=d2e78bbf822ca098393d50423eae7f6a&city=brackenfell'`

- 5 days weather results
`curl --location --request GET 'http://127.0.0.1:5000/forecasts/v1/daily/5day/?key=d2e78bbf822ca098393d50423eae7f6a&city=brackenfell'`


## Barchart

> you can see the barchart by visiting http://127.0.0.1:5000/forecasts/v1/daily/5day/barchart/?city=brackfenfell
