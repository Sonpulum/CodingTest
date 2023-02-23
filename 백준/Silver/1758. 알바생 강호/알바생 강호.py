import sys
n = int(sys.stdin.readline().strip())
l = sorted([int(sys.stdin.readline().strip()) for _ in range(n)],reverse=True)
q = [i for i in range(n)]

res = 0
for i in range(n):
    res += max(0,l[i]-q[i])

print(res)