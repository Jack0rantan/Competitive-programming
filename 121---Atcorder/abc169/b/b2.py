input = open('input.txt','r').readline

def main():
  n = int(input())
  ls = list(map(int, input().split()))
  if 0 in ls:
      print(0)
      return
  ans = 1
  for l in ls:
      ans *= l
      if ans > 1e18:
          print(-1)
          return
  print(ans)
  
main()