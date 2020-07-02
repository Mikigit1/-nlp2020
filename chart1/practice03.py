# “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，
# 各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

import collections
# charNum = collections.Counter(text)
# print(charNum)

text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

#単語の文字数カウント
text = text.replace(",", "").replace(".", "")
wordNum = [len(word) for word in text.split()]
print(wordNum)


#アルファベットの数カウント
counter = {}
for word in text:
    if not word in counter:
        counter[word] = 1
    else:
        counter[word] += 1

print(counter)