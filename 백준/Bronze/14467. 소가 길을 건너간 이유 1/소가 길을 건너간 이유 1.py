import sys
n = int(sys.stdin.readline().strip())
d = {}
cnt = 0

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a in d:
        if d[a] != b:
            cnt += 1
            d[a] = b
    else:
        d[a] = b

print(cnt)