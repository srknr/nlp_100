# coding: utf-8
#"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
#上の文を単語に分解、各単語の文字数を先頭から出現順に並べたリストを作成する

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
#空白でスライスしていって、文字の数字を確定
#for文で回して、len()で文字数を取得する。それらをリストに格納していく

s = str.find(' ')
print(s)#これは開始位置がわかるだけ
