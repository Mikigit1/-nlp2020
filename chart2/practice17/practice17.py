#1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはcut, sort, uniqコマンドを用いよ．

import pandas as pd

df = pd.read_table('chart2/popular-names.txt',header=None,names=['name','sex','number','year'])
col1 = df['name']

print(set(col1))