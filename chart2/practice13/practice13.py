'''
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．
'''
#col1・col2.txtの作成（practice12を参照）
import pandas as pd

df = pd.read_table('chart2/popular-names.txt',header=None,names=['name','sex','number','year'])
col1 = df['name']
clo1 = col1.to_csv('chart2/practice13/col1.txt',index=False)
col2 = df['sex']
col2 = col2.to_csv('chart2/practice13/col2.txt',index=False)

#ソースコード
col1 = pd.read_table('chart2/practice13/col1.txt')
col2 = pd.read_table('chart2/practice13/col2.txt')

merged_txt = pd.concat([col1,col2], axis = 1)
print(merged_txt.head())