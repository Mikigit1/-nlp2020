"""
“paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，
それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""

def nGramWord(text, num):
    #スライス
    result = [text[index : index+num ] for index in range(len(text)-num+1)]

    return result
    

#n_Gramに入れる
X = nGramWord("paraparaparadise", 2)
Y = nGramWord("paragraph",2)

print("Xのデータ:" + str(X))
print("Yのデータ"+ str(Y))

#set型のデータ
print("和集合")
print(set(X) | set(Y))
print("積集合")
print(set(X) & set(Y))
print("差集合")
print(set(X) - set(Y))

#'se'が含まれているかどうかの確認
print("Xに'se'は含まれているか？：" + str('se' in X))
print("Yに'se'は含まれているか？：" + str('se' in Y))

