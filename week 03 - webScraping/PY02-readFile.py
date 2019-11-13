# Test that you can read a file, carviewer2.html in ../carviewerTest folder 

from bs4 import BeautifulSoup

with open("../carviewerTest/carviewer2.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

print (soup.prettify())

'''
λ python PY02-readFile.py
<html>
 <head>
  <title>
   view Cars
  </title>
  <link crossorigin="anonymous" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" rel="stylesheet"/>
 </head>
 <body>
  <h1>
   Cars
  </h1>
  <div>
   <button id="showCreateButton" onclick="showCreate()">
    Create
   </button>
  </div>
  <div>
   <table class="table" id="carTable">
    <tr>
     <th>
      Reg
     </th>
     <th>
      Make
     </th>
     <th>
      Model
     </th>
     <th>
      Price
     </th>
     <th>
      Update
     </th>
     <th>
      Delete
     </th>
    </tr>
    <tr id="191 Mo 123">
     <td>
      191 Mo 123
     </td>
     <td>
      Ford
     </td>
     <td>
      Modeo
     </td>
     <td>
      25000
     </td>
     <td>
      <button onclick="showUpdate(this)">
       Update
	   
.
.
.
.
.
..
...

etc.

'''