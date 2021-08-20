import base64
from github import Github
from pprint import pprint

g = Github("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")
# Token cannot be made public :)

reponame = "TapanManu/PyGit"

def open_issue(reponame,title,body,assignee="TapanManu"):
    try:
        repo = g.get_repo(reponame)
        i = repo.create_issue(
            title = title,
            body = body,
            assignee = assignee
        )
        return i
    except:
        print("repository not found")
    return -1

def open_issues_list(reponame):
    # list of open issues
    repo = g.get_repo(reponame)
    open_issues = repo.get_issues(state = 'open')
    for i in open_issues:
        print(i)


def close_issue(reponame,i):
    try:
        repo = g.get_repo(reponame)
        ci = repo.get_issue(i.number)
        ci.edit(state='closed')
        print("closed the issue #",i.number)
    except:
        print("repository not found for closing")

x = open_issue(reponame, "Test run issue", "Test issue for github app")

