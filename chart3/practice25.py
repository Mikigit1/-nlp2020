'''
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ
'''

import pandas as pd
import re

df = pd.read_json("chart3/jawiki-country.json.gz", lines =  True)
print(df)

#text = df.query("title == 'イギリス'")["text"].values[0]→このままだと\nが邪魔
text = df.query("title == 'イギリス'")["text"].values[0].split("\n")
#print(text)で確認

#正規表現で２つにグループ化する
pattern = re.compile('\|(.+?)\s=\s(.+)')

#辞書型の用意
ans = {}

for line in text:
    result = re.search(pattern,line)
    if result: #trueの場合
        #print(result.group(1))→１を２に置き換えて確認
        ans[result.group(1)] = result.group(2)

print(ans)


'''
【参考】
https://ohke.hateblo.jp/entry/2019/01/12/230000 #queryについて
https://algorithm.joho.info/computer/wildcard-regular-expression/ #正規表現について
https://python.keicode.com/lang/regular-expression-use-search.php #searchの中身確認方法
https://note.nkmk.me/python-dict-add-update/ #辞書型の扱い
'''