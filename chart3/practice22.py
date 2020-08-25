# 必要なモジュールのインポート
import gzip
import json
import re

def search():
    with gzip.open('chart3/jawiki-country.json.gz',mode='rt',encoding='utf-8') as f:
        for line in f:
            json_load = json.loads(line)
            if json_load['title'] == 'イギリス':
                return json_load['text']

#findall(pattern, string)	正規表現にマッチする部分文字列を全て探しだしリストとして返します。
result = re.findall(r'^(.*\[\[Category:.*\]\].*)$',search(),re.MULTILINE)

    
for line in result:
    line = line.strip(r'^(.*\[\[Category:')
    line = line.strip(r'.*\]\].*)$')
    print(line.strip(r'.\|元$'))#無理やり