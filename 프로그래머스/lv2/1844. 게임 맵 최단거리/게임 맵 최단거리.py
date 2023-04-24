from collections import deque

def solution(maps):
    answer = 0
    m = len(maps)
    n = len(maps[0])
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]
    
    chk = [[0 for _ in range(n)]for _ in range(m)]
    chk[0][0] = 1
    
    q = deque()
    q.append((0,0))
    while q:
        ey, ex = q.popleft()
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if 0<= ny < m and 0<= nx <n:
                if maps[ny][nx] == 1:
                    if chk[ny][nx] == 0:
                        chk[ny][nx] = chk[ey][ex] + 1
                        q.append((ny,nx))
                    elif chk[ny][nx] > chk[ey][ex]+1:
                        chk[ny][nx] = chk[ey][ex]+1
                        q.append((ny,nx))

    answer = chk[m-1][n-1]
    if answer == 0:
        answer = -1
    
    return answer
        
    