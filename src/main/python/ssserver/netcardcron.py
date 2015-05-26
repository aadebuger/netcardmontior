'''
Created on 2015

@author: aadebuger
'''
from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler()
import time
def job_monitor():
    print 'job_montior'
def startMonitor():
    scheduler.add_job(job_monitor,'interval', minutes=1) 
    scheduler.daemonic = False 
    scheduler.start()
if __name__ == '__main__':
    print 'start Monitor'
    startMonitor()
    print 'end Monitor'
    time.sleep(5000)
    