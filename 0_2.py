# coding : utf-8
#パトカー+タクシー=パタトカクシーーを得る

import sys
#文字列の変数を置く、これらの文字列を交互に取り出して連結する。
str1 = "パトカー"
str2 = "タクシー"

#いま思いつくこと
#print(str1[0]+str[0]+...+str1[n]+str2[n])
#つまり1~nの中を回して連結させて足せばよい？
#print("str1の文字列の長さ" + len(str1))#これは型がintとstrになるのでうまくいってない
#print(len(str2))#これはうまくいく

for str in range(0, len(str1)):
    #print(str1[str]+str2[str])#これだと改行される
    sys.stdout.write(str1[str]+str2[str])#パタトクカシーー
    #print(str1[str]+str2[str], end="")#これでもok
print()#ターミナル用に改行
