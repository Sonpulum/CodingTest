import sys
from collections import deque

n = int(sys.stdin.readline().strip())
q = deque(map(int, sys.stdin.readline().split()))
s = deque([i for i in range(1,n+1)])
result = []

while q:
    v = q.popleft()
    result.append(s.popleft())
    if v >= 1:
        q.rotate(-v+1)
        s.rotate(-v+1)
    else:
        q.rotate(-v)
        s.rotate(-v)

print(*result)