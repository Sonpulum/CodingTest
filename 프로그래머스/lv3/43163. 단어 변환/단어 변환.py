from collections import deque

def solution(begin, target, words):
    answer = 0
    l = len(begin)
    words_len = len(words)
    chk = [False for _ in range(words_len)]
    
    q = deque()
    q.append((begin,0))
    while q:
        ew, ec = q.popleft()
        if ew == target:
            if answer == 0:
                answer = ec
            else:
                answer = min(answer,ec)
                
        for i in range(words_len):
            if able(ew,words[i],l):
                if chk[i] == False:
                    q.append((words[i],ec+1))
                    chk[i] = True

        
    return answer

def able(n,e,l):
    cnt = 0
    for i in range(l):
        if n[i] != e[i]:
            cnt += 1
        if cnt > 1:
            return False
    if cnt == 1:
        return True
    return False