import requests
from pprint import pprint

city = input('Enter a city: ')
api_key = "108b00f41bef416fb55141727220207"
url = "http://api.weatherapi.com/v1/current.json?key=" + api_key + "&q=" + city

response = requests.request("GET", url).json()

pprint(response)

