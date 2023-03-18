import sys
n, k = map(int, sys.stdin.readline().split())

s = sys.stdin.readline().strip()
chk = [False for _ in range(n)]
cnt = 0

for i in range(n):
  if s[i] == 'P':
    for j in range(-k,k+1):
      if 0<=i+j<n:
        if s[i+j] == 'H' and chk[i+j] == False:
          chk[i+j] = True
          cnt += 1
          break

print(cnt)