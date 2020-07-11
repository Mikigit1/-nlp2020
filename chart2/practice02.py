'''
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
'''

'''
unixコマンドは
sed -e 's/\t/ /g' chart2/popular-names.txt

（タブをスペースに変換）
tr '\t' ' ' chart2/popular-names.txt

(-tはタブ、1は置換したあと何個スペース空けるか)
expand -t 1 chart2/popular-names.txt
'''

with open('chart2/popular-names.txt','r') as file:
    for text in file:
        # タブ(\t)を 空白へ置換（strip空白（文字の間は別）を除去）
        print(text.strip().replace("\t"," "))
