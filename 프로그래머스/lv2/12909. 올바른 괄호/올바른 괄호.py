from collections import deque

def solution(s):
    answer = True
    s = deque(s)
    arr = deque()
    
    i = s.popleft()
    if i == ')':
        return False
    
    arr.append(i)
    while s:
        i = s.popleft()
        if i == ')':
            if arr:
                if arr[-1] == '(':
                    arr.pop()
            else:
                arr.append(i)
                
        else:
            arr.append(i)
    
    if arr:
        return False

    return True