import sys
from collections import deque

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    q = deque(list(map(int, sys.stdin.readline().split())))
    s = deque([i for i in range(n)])
    cnt = 0

    while q:
        if q[0] == max(q):
            cnt += 1
            q.popleft()
            if m == s.popleft():
                break

        else:
            q.rotate(-1)
            s.rotate(-1)
            
    print(cnt)