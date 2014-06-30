#!/usr/bin/python

import json, urllib.request, time

title = []

def pullInfo():
   

    rawdata = urllib.request.urlopen('http://www.reddit.com/r/todayilearned/new/.json').read()
    data = json.loads(rawdata.decode('utf8'))
    results = data['data']['children']

    for eachResult in results:
        
        if eachResult not in title:
            
            title.append(eachResult['data']['title'])
            print(eachResult['data']['title'], ' \n')
    

while True:
    pullInfo()
    print('***'*10)
    time.sleep(30)
