#!/usr/bin/python

import json, urllib.request, time, re

title = []


def urlcheck(x):
    try:
        rawdata = urllib.request.urlopen(x).read()
    except urllib.error.HTTPError:
        print('Unable to connect......retying')
        time.sleep(10)
        urlcheck(x)
    else:
        print(rawdata)
        return(rawdata)


def pullInfo():
   
    url = 'http://www.reddit.com/r/todayilearned/new/.json'
    rawdata = urlcheck(url)
    print(rawdata)
    data = json.loads(rawdata.decode('utf8'))
    results = data['data']['children']

    for eachResult in results:
        regResult = re.split("[Tt][Ii][Ll][,:\s]", eachResult['data']['title'])         
        if regResult[1] not in title:
           title.append(regResult[1].str.capitalize())
           print(regResult[1],'\n')
           
       
    

while True:
    pullInfo()
    print(len(title))
    print('***'*10)
    time.sleep(60)

