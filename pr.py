import base64
from github import Github
from pprint import pprint

username = "TapanManu"
g = Github("PASTE YOUR GITHUB ACCESS TOKEN HERE")
repo = g.get_repo("TapanManu/PyGit")
user = g.get_user(username)

def create_pull_request(repo,title,body):
    try:
        pr = repo.create_pull(title = title,
                              body = body,
                              head = "develop",
                              base = "main")
        print(pr)
    except:
        print("error creating pr")

def main():
    title = "Test PR using PyGithub"
    body = "SUMMARY: First PR"
    create_pull_request(repo, title, body)

main()
