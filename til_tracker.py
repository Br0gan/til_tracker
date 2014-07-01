#!/usr/bin/python

import json, urllib.request, time, re, csv


f = open('/home/corey/Docs/challenge/til_tracker/data/tildata.txt', 'a')


title = []


def urlcheck(address):
    try:
        rawdata = urllib.request.urlopen(address).read()
    except urllib.error.HTTPError:
        print('Unable to connect......retying')
        time.sleep(10)
        temp = urlcheck(address)
        return(temp)
    else:
        return(rawdata)


def pullInfo():
   
    url = 'http://www.reddit.com/r/todayilearned/new/.json'
    rawdata = urlcheck(url)
    data = json.loads(rawdata.decode('utf8'))
    results = data['data']['children']

    for eachResult in results:
        regResult = re.split("[Tt][Ii][Ll][,:\s-]", eachResult['data']['title'])
        urlResult = eachResult['data']['url']
        
        if (regResult[1], urlResult) not in title:
           title.append((regResult[1], urlResult))
           print(regResult[1].capitalize(),'\n',urlResult, '\n')
           print('****'*10)
           s = str(regResult[1]) + '\n' + str(urlResult) + '\n \n'
           f.write(s)

while True:
    pullInfo()
    time.sleep(60)

