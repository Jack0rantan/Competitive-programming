input = open('input.txt','r').readline

#-------------------------------
#   ミスポイント
#   a=1の時、b が幾つであっても
#   0を出力しなくてはいけなかった。
#-------------------------------
a, b = map(int, input().split())
count = a;ans = 1
while  b > count:
    count += a-1
    ans += 1
print(ans)
print(count)