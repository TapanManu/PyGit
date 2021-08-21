import base64
from github import Github
from pprint import pprint
import re

g = Github("GITHUB_ACCESS_TOKEN")
# Token cannot be made public :)

issue_dict = {}
reponame = "TapanManu/PyGit"

def get_comments(reponame,number):
    try:
        repo = g.get_repo(reponame)
        ci = repo.get_issue(number)
        return ci.get_comments()
    except:
        print("repository not found")

def get_reactions(reponame,number):
    try:
        repo = g.get_repo(reponame)
        issue = repo.get_issue(number)
        return issue.get_reactions()
    except:
        print("error")

def extract_users(body):
    #utility function to extract user mentions in utility functions
    body = re.sub(',#!$%^&*()',' ',body)
    list = body.split(' ')
    users = []
    for u in list:
        if u.startswith('@'):
            if u[1:] not in users:      # remove duplicate mentions
                users.append(u[1:])
    return users


issue_dict['comments'] = [comment for comment in get_comments(reponame, 14)]

#print(issue_dict['comments'][1].body)

print (issue_dict['comments'][1].user)

issue_dict['mentioned_users'] = [extract_users(comment.body) for comment in issue_dict['comments']]

#extracted user mentions in issue comments
print(issue_dict['mentioned_users'])



#issue_dict['reactions'] = [reaction for reaction in get_reactions(reponame,14)]
#print(issue_dict['reactions'])




