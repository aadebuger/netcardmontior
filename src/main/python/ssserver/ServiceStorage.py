'''
Created on 2015

@author: aadebuger
'''
from mongoengine import *

class ContainerService(Document):
    email = StringField(required=True)
    name =  StringField(required=True)
    containerid =  StringField(required=True)
#    first_name = StringField(max_length=50)
#    last_name = StringField(max_length=50)
    limit = IntField(required=True)
    

def getContainerServices():
        return ContainerService.objects
def getContainerServicebycontainerid(containerid):
        return ContainerService.objects(containerid=containerid)


def getContainerServicesdict():
      return   dict( map( lambda item: (item.containerid,item) , ContainerService.objects) )
    

def updateContainerServices(email,limit):
        containers = ContainerService.objects(email=email)
        containers.update_one(limit=limit)
#        containers[0].limit=limit
#        containers[0].update()
        
    
if __name__ == '__main__':
    connect('container',host="1257.net")
    testss = ContainerService(email="zhvxxh@gmail.com",limit=1000)
    
#    testss.save()