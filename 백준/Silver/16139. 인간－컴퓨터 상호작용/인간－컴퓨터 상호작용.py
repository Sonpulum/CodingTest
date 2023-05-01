import sys
s = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
for _ in range(n):
    t, b, e = map(str, sys.stdin.readline().split())
    b = int(b)
    e = int(e)
    print(s[b:e+1].count(t))