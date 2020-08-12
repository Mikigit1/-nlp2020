# coding: utf-8
import gzip
import json


'''
windows環境の場合、utf-8ではなく、cp932でコーディングされるため
with gzip.open('chart3/jawiki-country.json.gz',mode='rt', encoding = 'utf-8_sig') as f:
と記載する。
'''
with gzip.open('chart3/jawiki-country.json.gz',mode='rt') as f:
    for line in f:
        json_load = json.loads(line)
        if json_load['title'] == 'イギリス':
             print(json_load['text'])



        
            