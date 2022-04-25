This repository is made to delete all old build branches from the [osbm-cv](https://github.com/osbm/osbm-CV) repository. It is not meant to be used by anyone else. 

> [Note]():
> I just wanted to automate a task that takes a second. No wonder I can't get any shit done.

to use this action:

create the workflow file in your github repository as `.github/workflows/delete-old-build-branches.yml`

```yaml
name: Delete old build branches

on: [delete, workflow_dispatch]

jobs:
  deleter-job:
    name: Deleter job
    runs-on: ubuntu-latest
    steps:
      - name: Checkout the repository
        uses: actions/checkout@v3

      - name: Delete old branches
        uses: osbm/delete-old-build-branches@latest
        with:
          github_token: ${{ github.token }}
```