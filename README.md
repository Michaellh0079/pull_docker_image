# Overview
This commandline utility allows you to pull docker images from a GitLab registry by providing a GitLab username and 
GitLab access token

## Versioning
We are following `v<major>.<minor>.<patch>` versioning convention, where:
* `<major>+1` means we changed the infrastructure and/or the major components that makes this software run. Will definitely 
  lead to breaking changes.
* `<minor>+1` means we upgraded/patched the dependencies this software relays on. Can lead to breaking changes.
* `<patch>+1` means we fixed a bug and/or added a feature. Breaking changes are not expected.

# 🔨 Pre-requisite 
The utility attempts to read two environment variables: GIT_USERNAME and GIT_TOKEN. These values can be passed
to the script via command line arguments though. 


# How to
First install the requirements:
```commandline
pip install -r requirements.txt
```
Use ./pull_docker_image -h to view the help contents:
```commandline
./'pull_docker_image.py' -h
usage: pull_docker_image.py [-h] [-p TOKEN] [-t TAG] [-u USERNAME] registry

Pull a docker image from the GitLab registry.

positional arguments:
  registry              The registry to pull a docker image from

optional arguments:
  -h, --help            show this help message and exit
  -p TOKEN, --token TOKEN
                        A GitLab token with registry read privileges. Will attempt to retrieve this from the environment variable GIT_TOKEN.
  -t TAG, --tag TAG
  -u USERNAME, --username USERNAME
                        GitLab username. Will attempt to retrieve this fromthe environment variable GIT_USERNAME.
```
Example usage: 
```commandline
./pull_docker_image.py registry.gitlab.com/ghrc-cloud/ghrc-tf-deploy
Pulling latest image from registry.gitlab.com/ghrc-cloud/ghrc-tf-deploy...
```
