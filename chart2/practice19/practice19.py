'''
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ．
'''
import pandas as pd
df = pd.read_table('chart2/popular-names.txt',header=None,names=['name','sex','number','year'])
print(df['name'].value_counts(ascending=False))