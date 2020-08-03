# coding: utf-8
import gzip
import json

with gzip.open('chart3/jawiki-country.json.gz',mode='rt') as f:
    for line in f:
        json_load = json.loads(line)
        if json_load['title'] == 'イギリス':
             print(json_load['text'])
        
            