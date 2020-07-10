'''
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
'''

'''
wcコマンド
テキストファイルの行数や単語数（word count）、文字数を数えるコマンド
'''

count = 0
with open('chart2/popular-names.txt') as file:
    for line in file:
        count += 1

print(count)