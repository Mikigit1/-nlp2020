'''
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
確認にはtailコマンドを用いよ．
'''

import pandas as pd
df = pd.read_table('chart2/popular-names.txt',header=None,names=['name','sex','number','year'])

def output_tail(N):
    print(df.tail(N))

N = input("数字を入力してください>>")
output_tail(int(N))