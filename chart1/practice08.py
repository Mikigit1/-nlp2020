'''
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
'''


def cipher(sentense):
   secretList = list()

   for word in sentense:
        if word.islower():
           secretList.append(chr(219 - ord(word)))
        else:
           secretList.append(word)

   return  "".join(secretList)



sentense = input("英語で文章を入力してください　>>")
print(cipher(sentense))