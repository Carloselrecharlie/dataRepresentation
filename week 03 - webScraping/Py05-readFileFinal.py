# Put PY03-readOutFile.py and PY04 together to output the car info into a CSV file 

from bs4 import BeautifulSoup
# http://assets.londonist.com/uploads/2019/07/tube_pint_map.png

import csv
with open("../carviewerTest/carviewer2.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

#print (soup.tr) # not what we want
employee_file = open('carviwerData.csv', mode='w') 
# keeping the employee naming for ease of use
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

rows = soup.findAll("tr")
for row in rows:
    
    cols = row.findAll("td")
    dataList = []
    for col in cols[:-2]: # Added [:-2] to avoid update and delete -the last two elements in every element of cols- being outputed at the end of every line
        dataList.append(col.text)
    employee_writer.writerow(dataList)
employee_file.close()

# carviwerData.csv appears in the directory
    
