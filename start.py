from github import Github
import os
from pprint import pprint

token = os.getenv('GITHUB_TOKEN',"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")

g = Github(token)

repo = g.get_repo("TapanManu/PyGit")
try:
    branch = repo.get_branch("main")
    print(branch)
except:
    print("error fetching branch")