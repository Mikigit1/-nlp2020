#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
#この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．

#n-gram:unigramは一文字ずつ取り出す、bigramは二文字

text = "I am an NLPer"


def nGramWord(text, num):
    #スライス
    result = [text[index : index+num ] for index in range(len(text)-num+1)]

    return result


for i in range(1,5):
    print(str(i)+"番目")
    #単語n-gram
    print(nGramWord(text.split(),i))
    #文字n-gram
    print(nGramWord(text.replace(' ', ''),i))
