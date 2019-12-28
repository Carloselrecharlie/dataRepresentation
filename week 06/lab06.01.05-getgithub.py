# No token, public info only

import requests, json 

def getJSONFromUrl(url):
    response = requests.get(url)
    data = response.json()
    return data

url = "https://api.github.com/users?since=100" # shows logins
# url = "https://api.github.com/users/andrewbeattycourseware/followers" # checks followers of the repo()

data = getJSONFromUrl(url)
#print (data)
#Get the file name for the new file to write

filename = 'githubusers.json'

# If the file name exists, write a JSON string into the file.
if filename:
    # Writing JSON data
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

"""
Output from second url
 λ cat githubusers.json
[
    {
        "login": "MarianneLawless",
        "id": 36157521,
        "node_id": "MDQ6VXNlcjM2MTU3NTIx",
        "avatar_url": "https://avatars3.githubusercontent.com/u/36157521?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/MarianneLawless",
        "html_url": "https://github.com/MarianneLawless",
        "followers_url": "https://api.github.com/users/MarianneLawless/followers",
        "following_url": "https://api.github.com/users/MarianneLawless/following{/other_user}",
        "gists_url": "https://api.github.com/users/MarianneLawless/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/MarianneLawless/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/MarianneLawless/subscriptions",
        "organizations_url": "https://api.github.com/users/MarianneLawless/orgs",
        "repos_url": "https://api.github.com/users/MarianneLawless/repos",
        "events_url": "https://api.github.com/users/MarianneLawless/events{/privacy}",
        "received_events_url": "https://api.github.com/users/MarianneLawless/received_events",
        "type": "User",
        "site_admin": false
    },
    {
        "login": "ezekielonaloye-gmit",
        "id": 36563439,
        "node_id": "MDQ6VXNlcjM2NTYzNDM5",
        "avatar_url": "https://avatars2.githubusercontent.com/u/36563439?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/ezekielonaloye-gmit",
        "html_url": "https://github.com/ezekielonaloye-gmit",
        "followers_url": "https://api.github.com/users/ezekielonaloye-gmit/followers",
        "following_url": "https://api.github.com/users/ezekielonaloye-gmit/following{/other_user}",
        "gists_url": "https://api.github.com/users/ezekielonaloye-gmit/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/ezekielonaloye-gmit/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/ezekielonaloye-gmit/subscriptions",
        "organizations_url": "https://api.github.com/users/ezekielonaloye-gmit/orgs",
        "repos_url": "https://api.github.com/users/ezekielonaloye-gmit/repos",
        "events_url": "https://api.github.com/users/ezekielonaloye-gmit/events{/privacy}",
        "received_events_url": "https://api.github.com/users/ezekielonaloye-gmit/received_events",
        "type": "User",
        "site_admin": false
    },
	
	.
	.
	.
	.
	.
	
"""