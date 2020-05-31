f = open('input.txt','r')
input = f.readline


# --------------------------------------------------
# TLE になってしまった。
#   おそらく、index() や sort()は、
#   for文のような処理になるため、
#   O(n ** 2)時間かかっているのではないかと予測する
#       >>> 積極的にheapqを使おう。
# --------------------------------------------------

n, m = map(int,input().split())
s = list(map(int, input().split()))
for i in range(m):
    ms = max(s)
    idx = s.index(ms)
    s[idx] = ms//2
print(sum(s))
