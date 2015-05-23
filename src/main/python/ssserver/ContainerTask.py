'''
Created on 20150522

@author: aadebuger
'''

from celery import Celery
import os
from docker import Client

DOCKER_HOST = os.getenv('DOCKER_HOST', 'unix:///var/run/docker.sock')


app = Celery('tasks', broker='amqp://guest@%s//'%(os.getenv('celeryserver', "ci.1257.net")))

@app.task
def add(x, y):
    return x + y

@app.task
def stopContaineer( containerid):

    cli = Client(base_url=DOCKER_HOST)
    cli.stop(containerid)
if __name__ == '__main__':
    pass