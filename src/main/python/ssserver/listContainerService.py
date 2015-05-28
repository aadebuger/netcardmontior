'''
Created on 2015

@author: aadebuger
'''
import netcarddata
import ServiceStorage
from __builtin__ import True
def mapContainer(item,containerdict):
#    containerdict[item[0]]
    
    return (item[0],item[1]/1024,item[2]/1024,containerdict[item[0]].name,containerdict[item[0]].email)
def filterContainer(item,containerdict):
    try:
        containerdict[item[0]]
        return True
    except:
        return False
def listSscontainer():
            r= netcarddata.getRedis()
            keys = netcarddata.getKeys(r)
            news = netcarddata.getNetworkstats(r,keys)
#            netcarddata.processStats(news,10);
            statsv = netcarddata.getContainerStats(news);
            containerdict = ServiceStorage.getContainerServicesdict()
            newstatsv = filter(lambda item: filterContainer(item,containerdict),statsv)
            print 'newstatsv=',newstatsv
            sscontainerv= map(lambda item: mapContainer(item,containerdict),newstatsv)
            print 'sscontainerv=',sscontainerv
            for item in sscontainerv:
                print item,"\n"
            return sscontainerv
            
if __name__ == '__main__':
    listSscontainer()