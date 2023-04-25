from collections import deque

def solution(arr):
    answer = []
    arr = deque(arr)
    answer.append(arr.popleft())
    while arr:
        i = arr.popleft()
        if i != answer[-1]:
            answer.append(i)
            
    return answer