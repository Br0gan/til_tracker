#!/usr/bin/python

import json, urllib.request, time

title = []

def pullInfo():
   

    rawdata = urllib.request.urlopen('http://www.reddit.com/r/todayilearned/new/.json').read()
    data = json.loads(rawdata.decode('utf8'))
    results = data['data']['children']

    for eachResult in results:
       x = eachResult['data']['title']
       if x not in title:
           title.append(x)
           print(x)
       
    

while True:
    pullInfo()
    print(len(title))
    print('***'*10)
    time.sleep(60)

