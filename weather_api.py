import json, requests, statistics
from dotenv import load_dotenv
import os
import sys

API_KEY = os.environ.get("API_KEY")


class Weather:
	def __init__(self, city):
		self.city = city

	def get_city_key(self):

		url = "http://dataservice.accuweather.com/locations/v1/cities/search?apikey=" + API_KEY + "&q=" + self.city

		payload={}
		headers = {}

		response = requests.request("GET", url, headers=headers, data=payload)

		print(response)

		ckey = response.json()

		for c in ckey:
			return  c['Key']


	def get_one_day_forcast(self,city_key):

		url = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/"+ city_key +"?apikey=" + API_KEY + "&metric=true"

		payload={}
		headers = {}

		response = requests.request("GET", url, headers=headers, data=payload)

		forcast = response.json()

		my_forcasts = {'Forcasts': []} 
		for f in forcast['DailyForecasts']:
		
			# build up forcasts
			my_forcasts['Forcasts'].append({'Date': f['Date'], 'Min': f['Temperature']['Minimum']['Value'], 'Max': f['Temperature']['Maximum']['Value'] })
			

		json_object = json.dumps(my_forcasts)

		return json_object


	def get_five_day_forcast(self,city_key):
		url = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/"+ city_key +"?apikey=" + API_KEY + "&metric=true"

		payload={}
		headers = {}

		response = requests.request("GET", url, headers=headers, data=payload)

		forcast = response.json()

		#print(forcast)

		tlist_max = []
		tlist_min = []
		my_forcasts = {'Forcasts': [], 'Average_min': [], 'Avarage_max': [], 'Median_min': [], 'Median_max': []} 
		for f in forcast['DailyForecasts']:

			# min and max temp to calculate avareges
			tlist_min.append(f['Temperature']['Minimum']['Value'])
			tlist_max.append(f['Temperature']['Maximum']['Value'])
		
			# build up forcasts
			my_forcasts['Forcasts'].append({'Date': f['Date'], 'Min': f['Temperature']['Minimum']['Value'], 'Max': f['Temperature']['Maximum']['Value'] })

		# average calculations
		min_avg = statistics.mean(tlist_min)
		max_avg = statistics.mean(tlist_max)
		my_forcasts['Average_min'].append(min_avg)
		my_forcasts['Avarage_max'].append(max_avg)

		# median calculations
		med_min = statistics.median(tlist_min)
		med_max = statistics.median(tlist_max)
		my_forcasts['Median_min'].append(med_min)
		my_forcasts['Median_max'].append(med_max)

		"""
		Get the minimum Max value and maximum Max value.
		seeing that we already getting max and min values from the API 
		I wanted to get the max and min of the max and min LIST if you get what I'm saying here :-)
		
		I'm not returning this part to the JSON output of the API call as I thought maybe just leave it here
		so that you can see that I know how to do the calculations with build in functions.
		"""
		smallest_min = min(tlist_min)
		largest_min = max(tlist_min)

		smallest_max = min(tlist_max)
		largest_max = max(tlist_max)


		json_object = json.dumps(my_forcasts)

		return json_object


#w = Weather('brackenfell')

#the_key = w.get_city_key()

#print(w.get_one_day_forcast(the_key))
#print(w.get_five_day_forcast(the_key))