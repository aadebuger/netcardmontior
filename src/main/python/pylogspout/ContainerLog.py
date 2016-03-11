'''
Created on Mar 11, 2016

@author: aadebuger
'''
from docker import Client
import os
DOCKER_HOST = os.getenv('DOCKER_HOST', 'unix:///var/run/docker.sock')

def logContainer():
    cli = Client(base_url=DOCKER_HOST)
    print('cli',cli)
    cli.images()
if __name__ == '__main__':
    logContainer()