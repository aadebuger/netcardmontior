'''
Created on Mar 11, 2016

@author: aadebuger
'''
from docker import Client
from datetime import datetime
import os
DOCKER_HOST = os.getenv('DOCKER_HOST', 'unix:///var/run/docker.sock')

def logContainer():
    cli = Client(base_url=DOCKER_HOST)
    print('cli',cli)
    cli.images()
    line=""
    for c in cli.logs(os.getenv("logcontainer","mongodb0"), stderr=False, stream=True,since=datetime.now() ):
        line=line+c
        if c=='\n':
            print 'line=',line
            line=""
if __name__ == '__main__':
    logContainer()