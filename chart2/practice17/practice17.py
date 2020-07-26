#1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはcut, sort, uniqコマンドを用いよ．

import pandas as pd

df = pd.read_table('chart2/popular-names.txt',header=None,names=['name','sex','number','year'])
col1 = df['name']

def count_word(col1):
    counter = {}
    for word in col1:
        if not word in counter:
            counter[word] = 1
        else:
            counter[word] += 1
    return counter


print(count_word(col1))