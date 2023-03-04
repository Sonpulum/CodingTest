import sys

def input():
  return sys.stdin.readline().split()

n, m = map(int, input())
s = list(map(int, input()))

for _ in range(m):
  a,b,c = map(int, input())
  if a == 1:
    s[b-1] = c
    
  elif a == 2:
    for i in range(b-1,c):
      if s[i] == 0:
        s[i] = 1
      else:
        s[i] = 0

  elif a == 3:
    for i in range(b-1,c):
      s[i] = 0

  else:
    for i in range(b-1,c):
      s[i] = 1

print(*s)