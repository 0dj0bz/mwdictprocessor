# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv
import requests
import json
import pprint
import urllib

uri_base = "https://dictionaryapi.com/api/v1/references/"
mw_apikey = {"key":"5b6cac7e-5c02-41fa-8e72-b6d82d58bfa3"}
mw_resource = "collegiate"
lookupword = "test"

outpath = "/data2/diss/mw/dict/"
outputext = ".def"

base_querystr = uri_base + mw_resource + "/xml/"
    
#r = requests.get(querystr, urllib.parse.urlencode(mw_apikey))
wc = 0

with open('/data2/diss/mw/norvigwords.txt', newline='') as csvfile:
    words = csv.reader(csvfile, delimiter='\t')
    for word in words:
        querystr = base_querystr + word[0]
        print(querystr)
        r = requests.get(querystr, urllib.parse.urlencode(mw_apikey))
        
        with open(outpath+word[0]+outputext, 'w') as outfile:
            outfile.write(r.text)
            
        wc += 1
        # only process 1000 requests at a time per day
        if (wc >= 1000):
            break
        

