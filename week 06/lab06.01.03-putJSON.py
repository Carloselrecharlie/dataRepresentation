# Updates the record that matches the string -in url, after .../cars/ - with the new vales specified in dataString

import requests
import json

dataString = {'make':'BMW','model':'Kuga'}
url = 'http://127.0.0.1:5000/cars/test'

response = requests.put(url, json=dataString)

print (response.status_code)
print (response.text)


"""
Output:

200
{
  "car": {
    "make": "Ford",
    "model": "Kuga",
    "price": 8000,
    "reg": "test"
  }
}

"""