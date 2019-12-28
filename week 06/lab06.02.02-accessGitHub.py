# Get private data from github and create a json file with it (repo.json). From one of my repos, a private one created for testing purposes. 

import requests
import json


# enter your key here within ''
apiKey = ''
url = 'https://api.github.com/repos/Carloselrecharlie/aPrivateOne'
filename ="repo.json"

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()
#print (response.json())

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)

"""
 - If the token is wrong for whatever reason:

{
    "message": "Bad credentials",
    "documentation_url": "https://developer.github.com/v3"
}

"""