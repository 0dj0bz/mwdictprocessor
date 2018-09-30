# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import boto3
import csv
import requests
import json
import pprint
import urllib

uri_base = "https://dictionaryapi.com/api/v1/references/"
mw_apikey = {"key":"5b6cac7e-5c02-41fa-8e72-b6d82d58bfa3"}
mw_resource = "collegiate"
lookupword = "test"

wordfile_path = 'norvigwords.txt'

s3 = boto3.client('s3')


outpath = "./out/"
outputext = ".def"

base_querystr = uri_base + mw_resource + "/xml/"

start_row = 10000

#r = requests.get(querystr, urllib.parse.urlencode(mw_apikey))
wc = 0

with open(wordfile_path, newline='') as csvfile:

    words = csv.reader(csvfile, delimiter='\t')
    
    while words.line_num < start_row:
        words.__next__()
        
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
        

