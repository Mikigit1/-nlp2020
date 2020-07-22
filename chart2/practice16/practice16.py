'''
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
同様の処理をsplitコマンドで実現せよ．
'''

import pandas as pd
df = pd.read_table('chart2/popular-names.txt',header=None,names=['name','sex','number','year'])

def split_file(N):
    row = -(-len(df) // N)
    for i in range(N):
        print(df.loc[row * i: row * (i+1)])
        
N = input("分割行数を入力 >>")
split_file(int(N))

