'''
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
'''

'''
sedコマンド：Stream Editor
'''

with open('chart2/popular-names.txt','r') as file:
    for text in file:
        print(text.strip().replace("\t"," "))
