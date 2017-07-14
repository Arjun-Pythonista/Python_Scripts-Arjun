#Accessing Weather API from openweathemap.org in python
#By- Arjun

import requests
import json
from pprint import pprint as pp

def main():
  response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=London&appid=3493ce72bea8c66ef129fe372b7aff06&units=metric")
  weather = response.json()
  pp(weather)
  print("The weather for",weather['name'])
  print (weather['main']['temp'])



if __name__=='__main__':
    main()