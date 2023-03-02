import sys

n, m = map(int, sys.stdin.readline().split())

s = []
chk = [False for _ in range(n)]

def dfs(depth):
  if depth == m:
    print(' '.join(map(str,s)))
    return

  for i in range(1,n+1):
    s.append(i)
    dfs(depth+1)
    s.pop()

dfs(0)