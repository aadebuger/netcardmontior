'''
Created on 2015

@author: aadebuger
'''

from celery import Celery

app = Celery('hello', broker='amqp://guest@localhost//')

@app.task
def hello():
    return 'hello world'

if __name__ == '__main__':
    pass