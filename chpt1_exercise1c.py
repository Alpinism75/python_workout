#! /usr/bin/env

"""
Using a dictionary api
https://rapidapi.com/dpventures/api/wordsapi

"""

import requests

url = "https://wordsapiv1.p.rapidapi.com/words/"

querystring = {"random":"true"}

headers = {
    'x-rapidapi-key': "{key}",
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)