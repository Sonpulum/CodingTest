import sys
n = list(map(str, sys.stdin.readline().strip()))
ans = ''
for i in sorted(n, reverse=True):
    ans += i

print(int(ans))