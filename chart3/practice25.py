'''
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ
'''
#<ref>
import json
import re 
import gzip

def search():
    with gzip.open('chart3/jawiki-country.json.gz',mode='rt',encoding='utf-8') as f:
        for line in f:
            json_load = json.loads(line)
            if json_load['title'] == 'イギリス':
                return json_load['text']

match = re.findall(r'\[\[(ファイル):(.+?)\|',search())
for line in match:
    print(line)