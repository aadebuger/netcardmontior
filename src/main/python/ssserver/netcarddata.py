'''
Created on 20150518

@author: aadebuger
'''
import psutil
import redis 
import json
import os
print os.environ['HOME']
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
    r = redis.Redis(host=os.getenv('redisserver', "ci.1257.net"), port=6379, db=1) 
    
    return r
if __name__ == '__main__':
    r= getRedis()
    putRedisData(r)