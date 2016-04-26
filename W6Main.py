#!/usr/bin/python
# -*- coding: Cp1251 -*-

'''
Created on 26 апр. 2016 г.

@author: ggolyshev
'''

import json
import urllib.request

#serviceurl = 'http://python-data.dr-chuck.net/comments_42.json '
serviceurl = 'http://python-data.dr-chuck.net/comments_221449.json'

if __name__ == '__main__':
    address = input('Enter location: ')
    if len(address)<1:
        address=serviceurl
    print ('Retrieving', address)
    uh = urllib.request.urlopen(address)
    data=uh.read()
    print ('Retrieved %d characters' % len(data.decode('utf-8')))
    jinf=json.loads(data.decode('utf-8'))
    print ('Count : ', len(jinf['comments']))
    cnt=0
    for item in jinf['comments']:
        cnt+=(int(item['count']))
    print('Sum : ', cnt)