# -*- coding: utf-8 -*-
#%% Excersise 1

import requests
json_data = requests.get("https://api.lyrics.ovh/v1/queen/bohemian rhapsody").json()


print (json_data)
#%% Excersise 2

import requests

ISS = requests.get("http://api.open-notify.org/iss-now.json").json()


print (ISS["iss_position"]["longitude"])
print (ISS["iss_position"]["latitude"]) 

#%% Excersise 3

import requests
countries = requests.get("http://api.population.io:80/1.0/countries").json()


print (countries)
  
