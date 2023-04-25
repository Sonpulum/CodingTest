import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    res = 0
    cnt = 0
    
    while scoville:
        h1 = heapq.heappop(scoville)
        if h1 >= K:
            answer = cnt
            break
            
        if not scoville:
            answer = -1
            break
            
        h2 = heapq.heappop(scoville)*2
        res = h1 + h2
        heapq.heappush(scoville,res)
        cnt += 1

        
    return answer