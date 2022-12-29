import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    s = list(map(str, sys.stdin.readline().split()))
    for i in range(len(s)):
        tmp = ''
        for j in reversed(s[i]):
            tmp += j
        s[i] = tmp
    print(*s)