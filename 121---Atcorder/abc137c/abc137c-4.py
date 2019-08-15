dict = {}
ans = 0
for i in open("testinput_c.txt","r"):
    i = tuple(sorted(i))
    t = dict.get(i,0)
    dict[i] = t+1
    ans += t
    print(dict)
print(ans)
