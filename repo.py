import base64
from github import Github
from pprint import pprint

username = "TapanManu"
g = Github("PASTE YOUR GITHUB ACCESS TOKEN HERE")
repo = g.get_repo("TapanManu/PyGit")
user = g.get_user(username)

def get_contents(repo,path=""):
    # contents in root directory
    contents = repo.get_contents(path)
    for c in contents:
        print(c)

def get_commits(repo):
    commits = repo.get_commits()
    for c in commits:
        print(c)

def list_repo(user):
    # list all repos
    for repo in user.get_repos():
        print(repo)

def get_views(repo):
    traffic_per_week = repo.get_views_traffic(per='week')
    return traffic_per_week

def branch_list(repo):
    return list(repo.get_branches())

