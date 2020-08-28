import json
import re 
import gzip

def search():
    with gzip.open('chart3/jawiki-country.json.gz',mode='rt',encoding='utf-8') as f:
        for line in f:
            json_load = json.loads(line)
            if json_load['title'] == 'イギリス':
                return json_load['text']

def fileSearch(result):
    for file in result:
        print(file[1].strip(': |'))

#^(.*\[\[ファイル:.*\]\].*)$

result = re.findall(r'(\[\[ファイル)(.+?\|)',search())
print(fileSearch(result))