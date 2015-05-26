'''
Created on 2015

@author: aadebuger
'''
from mongoengine import *

class ContainerService(Document):
    email = StringField(required=True)
#    first_name = StringField(max_length=50)
#    last_name = StringField(max_length=50)
    limit = IntField(required=True)

def getContainerServices():
        return ContainerService.objects
    
if __name__ == '__main__':
    connect('container',host="1257.net")
    testss = ContainerService(email="zhvxxh@gmail.com",limit=1000)
    testss.save()