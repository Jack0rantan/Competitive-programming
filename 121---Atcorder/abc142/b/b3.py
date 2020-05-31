f = open('input.txt','r')
input = f.readline


#-------------------
# b2.py の検証・解説
#-------------------

# 無名関数を定義している
# lamda ; define the Closure as 'R'
R = lambda:list(map(int,input().split()))
input()
# 無名関数を使うことで見栄えよく入力を処理している。
a, b, c = R(), R(), R()
#print(a,b,c)

# zip()は複数のイテラブルオブジェクトの要素をまとめる関数
# for文で複数の要素を取り出すときに使う
# a[1] == a[0] + 1　であれば
# sum(c[a[i]] - 1)
# としているので、やっていることは b.py　と同じ処理。
print(sum(b) + sum(c[i - 1] for i, j in zip(a, a[1:]) if j == i + 1))

# print(list(i-1 for i, j in zip(a, a[1:]) if j == i + 1))
