import os

from github import Github
from github.GithubException import GithubException

g = Github(os.environ["INPUT_GITHUB_TOKEN"])
repo = g.get_repo("osbm/osbm-CV")
branches = repo.get_branches()
branch_names = [branch.name for branch in branches]

branches_to_prune = []
for branch in branch_names:
    if branch[:7] == "build-" and branch[7:] not in branch_names:
        branches_to_prune.append(branch)


for branch in branches:
    if branch.name in branches_to_prune:
        print(f"Deleting branch {branch.name}")
        print(branch)
