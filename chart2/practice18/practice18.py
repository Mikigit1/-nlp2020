'''
18. 各行を3コラム目の数値の降順にソートPermalink
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）
'''
import pandas as pd

df = pd.read_table('chart2/popular-names.txt',header=None,names=['name','sex','number','year'])
print(df.sort_values('number',ascending=False))