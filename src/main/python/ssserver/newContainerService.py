'''
Created on 2015

@author: aadebuger
'''
import ServiceStorage

from mongoengine import *
import sys
if __name__ == '__main__':
    
    if len(sys.argv)<5:
        print 'python email,name,containerid,limit'
        sys.exit()
    connect('container',host="1257.net")
    
    testss = ServiceStorage.ContainerService(email=sys.argv[1],name=sys.argv[2],containerid=sys.argv[3],limit=int(sys.argv[4]))
    testss.save()