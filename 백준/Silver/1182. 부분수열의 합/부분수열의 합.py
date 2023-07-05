import sys

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
chk = [False for _ in range(n)]
result = []
cnt = 0


def perm(start):
  global cnt

  if result and sum(result) == s:
    cnt += 1
  for i in range(start, n):
    if chk[i]:
      continue
    result.append(arr[i])
    chk[i] = True
    perm(i)
    chk[i] = False
    result.pop()

perm(0)
print(cnt)