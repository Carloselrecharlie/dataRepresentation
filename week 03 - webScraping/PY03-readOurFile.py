
# Extract the first <tr> from the file 

from bs4 import BeautifulSoup

with open("../carviewerTest/carviewer2.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

'''
#print (soup.tr) # this does not print what we intend

λ python PY03-readOurFile.py  
<tr>                          
<th>Reg</th>                  
<th>Make</th>                 
<th>Model</th>                
<th>Price</th>                
<th>Update</th>               
<th>Delete</th>               
</tr>                         
'''
rows = soup.findAll("tr")
for row in rows:
    #print("-------")
    #print(row)
    dataList = []
    cols = row.findAll("td")
    for col in cols:
        dataList.append(col.text)
    print (dataList)


'''
λ python PY03-readOurFile.py
[]
['191 Mo 123', 'Ford', 'Modeo', '25000', 'Update', 'Delete']
['12 G 123', 'Fiat', 'Punto', '12', 'Update', 'Delete']
['05 D 123', 'Nissan', 'Almera', '500', 'Update', 'Delete']
'''