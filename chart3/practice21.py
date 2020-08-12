# coding: utf-8
import gzip
import json
#正規表現使うためのライブラリ
import re

'''
windows環境の場合、utf-8ではなく、cp932でコーディングされるため
with gzip.open('chart3/jawiki-country.json.gz',mode='rt', encoding = 'utf-8_sig') as f:
と記載する。
'''
def search_UK():
    with gzip.open('chart3/jawiki-country.json.gz',mode='rt') as f:
        for line in f:
            json_load = json.loads(line)
            if json_load['title'] == 'イギリス':
                return json_load['text']


#findall(pattern, string)	正規表現にマッチする部分文字列を全て探しだしリストとして返します。
result = re.findall(r'^(.*\[\[Category:.*\]\].*)$',search_UK(),re.MULTILINE)

for line in result:
    print(line)