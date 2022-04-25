import os

from github import Github
from github.GithubException import GithubException

# get the token from the environment variable
token = os.environ['GITHUB_TOKEN']
for k, v in sorted(os.environ.items()):
    print(k+':', v)
print('\n')
# list elements in path environment variable
[print(item) for item in os.environ['PATH'].split(';')]


# get the repo name from the environment variable
# repo_name = os.environ['GITHUB_REPOSITORY']
# print(f"{repo_name = }")

# get all branches
"""
g = Github(token)
repo = g.get_repo('osbm/osbm-CV')
branches = repo.get_branches()
print(f"{branches = }")
"""
