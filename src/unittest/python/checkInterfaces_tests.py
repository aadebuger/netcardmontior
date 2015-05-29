'''
Created on 2015

@author: aadebuger
'''
import unittest
from ssserver import netcarddata

class Test(unittest.TestCase):


    def testName(self):
        netcarddata.checkInterfaces()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()