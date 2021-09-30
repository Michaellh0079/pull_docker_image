#!/usr/bin/env python
import argparse
import os

import docker


def main():
    parser = argparse.ArgumentParser(description='Pull a docker image from the GitLab registry.')
    parser.add_argument('-p', '--token', required=False, default=os.getenv('GIT_TOKEN'),
                        type=str, help='A GitLab token with registry read privileges. Will attempt to retrieve this '
                                       'from the environment variable GIT_TOKEN.')
    parser.add_argument('registry', type=str, help='The registry to pull a docker image from')
    parser.add_argument('-t', '--tag', required=False, default='latest', type=str, help='')
    parser.add_argument('-u', '--username', required=False, default=os.getenv('GIT_USERNAME'),
                        type=str, help='GitLab username. Will attempt to retrieve this from'
                                       'the environment variable GIT_USERNAME.')

    args = parser.parse_args()
    client = docker.DockerClient()
    client.login(registry=args.registry, username=args.username, password=args.token)
    print(f'Pulling {args.tag} image from {args.registry}...')
    client.images.pull(repository=args.registry, tag=args.tag)


if __name__ == '__main__':
    main()
