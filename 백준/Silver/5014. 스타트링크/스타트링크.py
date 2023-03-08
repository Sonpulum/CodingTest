import sys
from collections import deque

f, s, g, u, d = map(int, sys.stdin.readline().split())
chk = [False for _ in range(f+1)]
dir = [u,-d]

def bfs():
    q = deque()
    q.append([s,0])
    chk[s] = True
    while q:
        e = q.popleft()
        i, cnt = e
        for j in range(2):
            n = i+dir[j]
            if 1<=n<=f:
                if chk[n] == False:
                    chk[n] = True
                    q.append([n,cnt+1])
                    if n == g:
                        print(cnt+1)
                        return
    
    print("use the stairs")
    return

if g == s:
    print(0)
else:
    bfs()
