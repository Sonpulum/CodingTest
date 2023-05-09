n = int(input())

result = []
chk = [False for _ in range(n+1)]

def permutation(depth):
  if depth == n:
    print(*result)
    return
  for i in range(1,n+1):
    if chk[i]:
      continue
    result.append(i)
    chk[i] = True
    permutation(depth+1)
    chk[i] = False
    result.pop()

permutation(0)