
#Test that we can retrieve a web page from the web http://dataquestio.github.io/web-scraping-pages/simple.html 

import requests
from bs4 import BeautifulSoup
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print (page) #prints response
print("-------------------")
print (page.content) #prints source code L18


#Test that BeautifulSoup is installed by modifying the program to read

soup1 = BeautifulSoup(page.content, 'html.parser')
print (soup1.prettify()) # prettify for a nice format


'''
λ python PY01-testRequest.py
<Response [200]>
-------------------
b'<!DOCTYPE html>\n<html>\n    <head>\n        <title>A simple example page</title>\n    </head>\n    <body>\n        <p>Here is some simple content for this page.</p>\n
</body>\n</html>'
<!DOCTYPE html>
<html>
 <head>
  <title>
   A simple example page
  </title>
 </head>
 <body>
  <p>
   Here is some simple content for this page.
  </p>
 </body>
</html>
'''