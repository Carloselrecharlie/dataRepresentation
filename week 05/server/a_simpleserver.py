#!flask/bin/python
from flask import Flask

# Enabling app server to serve static pages with the three lines below
app = Flask(__name__,
            static_url_path='', 
            static_folder='../') # It looks into the parent folder of the server. So you can open a file from the app server parent folder by adding it's file name at the end of the URL http://127.0.0.1:5000/

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__' :
    app.run(debug= True)
	

'''
returned from command line:
127.0.0.1 - - [14/Nov/2019 13:18:14] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [14/Nov/2019 13:18:15] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [14/Nov/2019 13:31:03] "GET /index HTTP/1.1" 404 -
127.0.0.1 - - [14/Nov/2019 13:31:22] "GET /index.html HTTP/1.1" 200 -
'''