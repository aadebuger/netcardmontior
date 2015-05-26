'''
Created on 20150518

@author: aadebuger
'''
import psutil
import redis 
import json
import os
from __builtin__ import True
print os.environ['HOME']
def filterflow(item ):
    name,value =item;
    print 'name=',name
    print 'value=',value,value[0],value[1]
    if value[0]+value[1]>1024*1000*1000L:
            return True
    return False
    
def putData():
    ret=psutil.net_io_counters(pernic=True)
    print 'ret=',ret
    for item in ret:
        print 'item=',item,ret[item],json.dumps(ret[item])
    return ret
def putRedisData(r):
    ret=psutil.net_io_counters(pernic=True)
    print 'ret=',ret
    for item in ret:
        print 'item=',item,ret[item],json.dumps(ret[item])
        r.set(item,json.dumps(ret[item]))
    return ret
def getRedis():  
    r = redis.Redis(host=os.getenv('redisserver', "ci.1257.net"), port=6379, db=8) 
    
    return r
def checkInterfaces():
    ret=psutil.net_io_counters(pernic=True)
    print 'ret1=',ret
    retm = map(lambda x: (x,ret[x]), ret)
#    print 'retm=',retm
    retm1 =filter(filterflow,retm);
    print 'retm1=',retm1
    print retm;
def getStats(r,key):
    ret=r.get(key)
    print 'ret=',ret

def filterKeys(item ):
    print 'item=',item
    return True
def getKeys(r):
    keys=r.keys("*")
    skeys = sorted(keys)
    if len(skeys)>0:
        key = skeys[-1]
        print 'key=',key
        print 'timeline=',key[:12]
        skeys=filter(lambda item: item.startswith(key[:12])and item.endswith("network"),skeys)
        
    print 'skeys=',skeys
    return skeys
def getNetworkstats(r,keys):
    print 'keys=',keys
    news =map(lambda item:(item,r.get(item)),keys)
    print 'stats=',news
    return news;
def overflowlimit(bytes,limit):
    if bytes>limit:
        return True
    return False
def processStats(news,limit):
    print 'procesStats'
    ipbytes = map(lambda item: (item[0],json.loads(item[1])),news)
    print 'ipbytes=',ipbytes
#    ipbytes1 = map(lambda item: item["rx_bytes"],ipbytes)
#    print 'ipbytes1=',ipbytes1
    retv = filter(lambda item: overflowlimit(item[1]["rx_bytes"]+item[1]["tx_bytes"],limit),ipbytes)   
    print "container=",retv
if __name__ == '__main__':
    r= getRedis()
#    putRedisData(r)
    checkInterfaces()