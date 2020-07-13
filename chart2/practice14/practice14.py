'''
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
確認にはheadコマンドを用いよ．
'''

import pandas as pd
#tableの作成
df = pd.read_table('chart2/popular-names.txt',header=None,names=['name','sex','number','year'])


def output_head(N):
    print(df.head(N))

N = input("数字を入力してください>>")
output_head(int(N))