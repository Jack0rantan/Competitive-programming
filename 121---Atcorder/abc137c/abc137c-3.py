dict = {}
ans = 0
for i in open("testinput_c.txt","r"):
    i = tuple(sorted(i))
    t = dict.get(i,0)
    ans += t
    dict[i] = t+1
    print(dict)
print(ans)
