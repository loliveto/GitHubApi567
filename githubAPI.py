import requests
import json

def func(userID):
    site = "https://api.github.com/users/"+userID+"/repos"
    r = requests.get(site)
    data = r.json()
    print(data[1]["name"])

    for repo in data:
        csite = "https://api.github.com/repos/"+userID+"/"+repo["name"]+"/commits"
        cr = requests.get(csite)
        cdata = cr.json()
        print("Repo: "+repo["name"]+" Number of commits: "+str(len(cdata)))

if __name__ == "__main__":
    func("richkempinski")