input = open('input.txt','r').readline


import heapq
N, M = map(int, input().split())
A = list(map(int, input().split()))


# A のすべての要素に '-1'を掛けている
# heapq.popが最小の要素を取り出すため、最大の要素を取り出すには
# あらかじめ正負を逆転しておくってこと。
Ai = list(map(lambda x: x*(-1), A))
# heapq.heapify(x)
#   リストxをヒープに変換します
#   in-place処理なので処理速度はO(log(n))
heapq.heapify(Ai)

for i in range(M):
    # heapq.heappop(x)
    #    ポップを行い、heap から "最小" の要素を取り出す。
    #    わざわざソートする必要もなく、取り出せる。優秀だ。
    #    heap[0]でも最小の要素にアクセス可能だとか？　詳しくは公式Document
    maxA = heapq.heappop(Ai)*(-1)
    waribiki = maxA // 2
    # heapq.heappush(x, item)
    #    ヒープxにitemをプッシュします
    heapq.heappush(Ai,waribiki * (-1))
    #print(Ai)
  
print(sum(Ai) * (-1))