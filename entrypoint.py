import os

from github import Github
from github.GithubException import GithubException

# get the token from the environment variable
# token = os.environ['GITHUB_TOKEN']



# get the repo name from the environment variable
# repo_name = os.environ['GITHUB_REPOSITORY']
# print(f"{repo_name = }")

# get all branches

g = Github(os.environ["INPUT_GITHUB_TOKEN"])
repo = g.get_repo('osbm/osbm-CV')
branches = repo.get_branches()
for branch in branches:
    print(branch.name)

print(f"{branches = }")

