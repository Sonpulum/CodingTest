import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
q = deque([i for i in range(1,n+1)])
result = []

while q:
    q.rotate(-k+1)
    result.append(q.popleft())

print("<"+", ".join(str(i) for i in result) + ">")