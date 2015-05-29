'''
Created on 

@author: aadebuger
'''
import unittest
from ssserver import netcarddata

class Test(unittest.TestCase):


    def testName(self):
            r= netcarddata.getRedis()
            netcarddata.getStats(r,"201505200337:935d84b383cf:network")
    def testGetkeys(self):
            r= netcarddata.getRedis()
            keys = netcarddata.getKeys(r)
            news = netcarddata.getNetworkstats(r,keys)
#            netcarddata.processStats(news,10);
            netcarddata.processStats(news,1000000);
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()