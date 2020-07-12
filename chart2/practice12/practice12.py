'''
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

【参考URL】
https://pythondatascience.plavox.info/pandas/%E3%83%87%E3%83%BC%E3%82%BF%E3%83%95%E3%83%AC%E3%83%BC%E3%83%A0%E3%82%92%E5%87%BA%E5%8A%9B%E3%81%99%E3%82%8B
https://takuya-1st.hatenablog.jp/entry/2014/08/04/150300

cutコマンド
cut -f 1 chart2/popular-names.txt
cut -f 2 chart2/popular-names.txt

'''

#ソースコード
import pandas as pd

df = pd.read_table('chart2/popular-names.txt',header=None,names=['name','sex','number','year'])
col1 = df['name']
col1.to_csv('chart2/practice12/col1.txt',index=False)
col2 = df['sex']
col2.to_csv('chart2/practice12/col2.txt',index=False)

print(df)