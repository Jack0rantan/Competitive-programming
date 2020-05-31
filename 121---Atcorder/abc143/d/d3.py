input = open('input.txt','r').readline

# from fractions import *
from math import gcd

# fractions は 有理数(分数) を計算するためのlibraryである。
# 現在は非推奨のライブラリ、代わりに math を使う
# AtCorder では math　を　import できない。そのため、fractionsを使う。 
# ここでは gcd() を使うためだけ
# https://note.nkmk.me/python-fractions-usage/
# 
# なお、 import * は　fractionsライブラリの中にあるmoduleを
# すべて、そのままの名称でimportするということ。
#  (__で始まるmoduleを覗く。)
#   https://medium.com/@s16h/importing-star-in-python-88fe9e8bd4d2
# 

g =gcd(*map(int,input().split()))
# gcd() は　ユークリッドの互除法で最大公約数を返却するmethod

d={}
# dictionary を用意
i=2
# これは　素因数分解　を考える問題。
# 以下は「試し割り法(Trial Division)」を扱っている。
# 「試し割り法」はフィボナッチが説明した手法でもあるらしい。
# https://en.wikipedia.org/wiki/Trial_division
# https://note.nkmk.me/python-prime-factorization/
while i**2 <= g:
    # i**2 <= g
    #    計算時間を減らすための工夫ポイント。
    # 　　　
    # 　　
    if g%i:
        ## 最大公約数 g が i で割り切れない場合
        # 例えば g = 99の時、
        # i = 2 は 公約数ではない ため、対象から外せる
        #  ---> i = 3　に遷移する。
        i+=1
    else:
        ## 最大公約数 g が i で割り切れた場合
        # 逆に言えば、g は i で割り切れてしまうため、対象から外せる。
        # 　　　---> g//=i
        # さらに、i は 2から１ずつ増えるが、割り切れているなら
        # 素因数であると言える。
        #  
        # 例えば g = 99 の時、
        # i = 3 -> g = 33
        # i = 3 -> g = 11
        # と２回カウントするケースがある。
        # この場合は２回出現した、と辞書に記載する。
        
        # 下記の表記は
        #     g = g//i
        #          と同じ
        # 99(i = 3) -> 33(i = 3) -> 11 となりブレイクする。 
        g //= i
        
        # 辞書.get(a , b) は
        # 辞書のなかに value = a があればそれを取り出す。
        # 　　　　　　　　なければ、b を返却するメソッド 。
        #  
        d[i]=d.get(i,0)+1
        

# 最大公約数が 1 のケース　g=1　以外。
# 上記の処理では 互いに素である最大の公約数を辞書に入れず break するので
# 下記で最後の数字を入れてやる。
if g>1:
    # 
    d[g]=d.get(g,0)+1

# 最後に 1 を足すのは上記処理ではi=１を除いた公約数を考えているので、
# 公約数1を考慮させる。 
print(len(d)+1)
