'''
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文
（例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）
を与え，その実行結果を確認せよ．
'''
import random

'''
ランダムに複数の要素を選択（重複なし）: random.sample()
randomモジュールの関数sample()で、リストからランダムで複数の要素を取得できる。要素の重複はなし（非復元抽出）。

第一引数にリスト、第二引数に取得したい要素の個数を指定する。リストが返される。
'''

def randomSort(word):
     if len(word) <= 4:
         return word
     else:
         text = random.sample(list(word[1:-1]),len(word[1:-1]))
         return ''.join([word[0]] + text + [word[-1]])


sentense = input("英文を入力してください>>")
ans = [randomSort(word) for word in sentense.split()]

print(' '.join(ans))

'''
元のリストをシャッフル: random.shuffle()
randomモジュールの関数shuffle()で、元のリストをランダムに並び替えられる。
'''

#解答2
result = []
def Typoglycemia(target):
    for word in target.split(' '):
        if len(word) <= 4:
            result.append(word)
        else:
            chr_list = list(word[1:-1])
            random.shuffle(chr_list)
            result.append(word[0] + ''.join(chr_list) + word[-1])

    return ' '.join(result)

# 対象文字列の入力
target = input('文字列を入力してください--> ')

# タイポグリセミア
result = Typoglycemia(target)
print('変換結果:' + result)