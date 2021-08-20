import base64
from github import Github
from pprint import pprint

g = Github("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")
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

issue_dict['comments'] = [comment for comment in get_comments(reponame, 14)]

print(issue_dict['comments'])

print (issue_dict['comments'][0].user)


#issue_dict['reactions'] = [reaction for reaction in get_reactions(reponame,14)]
#print(issue_dict['reactions'])




