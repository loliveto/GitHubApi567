# Laura Oliveto
# I pledge my honor that I have abided by the Stevens Honor System
import requests
import json

"""
The display function will take in a github user ID and display
all of the repositories associated with that account, along
with the number of commits made to that repository.
"""
def display(userID):
    # Grabs the json object from the site, and turns it into a
    # usable dictionary
    site = "https://api.github.com/users/"+userID+"/repos"
    r = requests.get(site)
    data = r.json()
    # The list that will be used to easily test the data
    testlist = []
    for repo in data:
        #print(userID + ": " + repo)
        csite = "https://api.github.com/repos/"+userID+"/"+repo["name"]+"/commits"
        cr = requests.get(csite)
        cdata = cr.json()
        print("Repo: "+repo["name"]+" Number of commits: "+str(len(cdata)))
        testlist.append((str(repo["name"]), len(cdata)))

    return testlist

if __name__ == "__main__":
    display("nhilden1114")
    display("loliveto")
    display("richkempinski")