import os

from github import Github
from github.GithubException import GithubException
from github.GithubException import UnknownObjectException

g = Github(os.environ["INPUT_GITHUB_TOKEN"])
repo = g.get_repo(os.environ["GITHUB_ACTION_REPOSITORY"])
branches = repo.get_branches()

# thanks to https://github.com/abulka in
# https://github.com/PyGithub/PyGithub/issues/1260
def delete_branch(branch_name):
    try:
        ref = repo.get_git_ref(f"heads/{branch_name}")
        ref.delete()
    except UnknownObjectException:
        print('No such branch', branch_name)

branch_names = [branch.name for branch in branches]

build_branches = [branch for branch in branch_names if branch.startswith("build-")]

for branch in build_branches:
    if branch[7:] not in branch_names: # these are good branches
        print(f"Deleting branch {branch}")
        delete_branch(branch)
