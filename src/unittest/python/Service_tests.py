'''
Created on 2015

@author: aadebuger
'''
import unittest
from ssserver import ServiceStorage
from ssserver import ServiceStorage

from mongoengine import *

class Test(unittest.TestCase):


    def testName(self):
        connect('container',host="1257.net")
        retv =ServiceStorage.getContainerServices()
        print 'retv=',retv
        for item in retv:
           print 'item=',item,'item containerid',item.containerid, item.email,"limit",item.limit
        retdict = ServiceStorage.getContainerServicesdict()
        print 'retdict=',retdict
    def testgetContainerServicebycontainerid(self):
        
        print 'container=',ServiceStorage.getContainerServicebycontainerid("5327e7f30452")
        print 'container=',ServiceStorage.getContainerServicebycontainerid("5327e7f30452")[0]
        print 'container=',ServiceStorage.getContainerServicebycontainerid("5327e7f30452")[0].name
        
        
    def testUpdate(self):
        ServiceStorage.updateContainerServices("zhvxxh@gmail.com",500)

#        print 'container=',container

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()