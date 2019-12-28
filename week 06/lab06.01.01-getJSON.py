# Gather all the cars, print it in the console in two different ways and create two files, json and excel ones. First run restserver!

import requests
import json
from xlwt import *

url = "http://127.0.0.1:5000/cars"

response = requests.get(url)
data = response.json()

#output to console
print (data)
#{'cars': [{'make': 'Ford', 'model': 'Modeo', 'price': 18000, 'reg': '181 G 1234'}, {'make': 'Nissan', 'model': 'Almera', 'price': 8000, 'reg': '11 MO 1234'}, {'make': 'Nissan', 'model': 'Almera', 'price': 8000, 'reg': 'test'}]}


#output cars individualy 
for car in data["cars"]:
    print (car)
"""
{'make': 'Ford', 'model': 'Modeo', 'price': 18000, 'reg': '181 G 1234'}
{'make': 'Nissan', 'model': 'Almera', 'price': 8000, 'reg': '11 MO 1234'}
{'make': 'Nissan', 'model': 'Almera', 'price': 8000, 'reg': 'test'}
"""

#other code
#save this to a file
filename = 'cars.json'
if filename:
    # Writing JSON data
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# write to excel file
w = Workbook()
ws = w.add_sheet('cars')
row = 0;
ws.write(row,0,"reg")
ws.write(row,1,"make")
ws.write(row,2,"model")
ws.write(row,3,"price")
row += 1 
for car in data["cars"]:
    ws.write(row,0, car["reg"])
    ws.write(row,1,car["make"])
    ws.write(row,2,car["model"])
    ws.write(row,3,car["price"])
    row += 1

w.save('cars.xls')