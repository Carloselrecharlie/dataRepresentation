# Commit changes to a repo. Add a line in the readme.md file and commit it

# to use this install package
# pip install PyGithub
from github import Github
import requests

# enter your key here within ""
g = Github("")

#for repo in g.get_user().get_repos():
#    print(repo.name)
    #repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    #print(dir(repo))
repo = g.get_repo("Carloselrecharlie/aPrivateOne")
#print(repo.clone_url)
fileInfo = repo.get_contents("README.md")
urlOfFile = fileInfo.download_url
#print (urlOfFile)
response = requests.get(urlOfFile)
contentOfFile = response.text
#print (contentOfFile)
newContents = contentOfFile + " \n This new line was created through a pyhton script \n"
print (newContents)
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print (gitHubResponse)

"""
λ python lab06.03.01-githubbymodule.py
# aPrivateOne
test

This private repository is just to test github API
 more stuff

 This new line was created through a pyhton script

{'commit': Commit(sha="e183045c0408abc289a32842dafb787b8718e627"), 'content': ContentFile(path="README.md")}

"""
