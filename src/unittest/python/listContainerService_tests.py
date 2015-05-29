'''
Created on 2015

@author: aadebuger
'''
import unittest

from ssserver import listContainerService
from mongoengine import *

class Test(unittest.TestCase):


    def testListSscontainer(self):
        print 'testListSscontainer='
        connect('container',host="1257.net")
        listContainerService.listSscontainer()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testListSscontainer']
    unittest.main()