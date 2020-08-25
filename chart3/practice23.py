'''
記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．
'''
# 必要なモジュールのインポート
import gzip
import json
import re

def search():
    with gzip.open('chart3/jawiki-country.json.gz',mode='rt') as f:
        for line in f:
            json_load = json.loads(line)
            if json_load['title'] == 'イギリス':
                return json_load['text']

def count(text):
    
print(count(search()))