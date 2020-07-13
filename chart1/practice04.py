'''
“Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”という文を単語に分解し，
 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
'''

text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
text = text.replace(",","").replace(".","").split()


def wordTake(num , word):
    if num in [1,5,6,7,8,9,15,16,19]:
        return (word[0],num)
    else:
        return(word[:2],num)

#enumerate関数の使用
ans = [wordTake(num,word) for num , word in enumerate(text,1)]

print(dict(ans))
