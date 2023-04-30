import sys
import heapq
n = int(sys.stdin.readline().strip())
heap = []
for _ in range(n):
    c = int(sys.stdin.readline().strip())
    if c != 0:
        heapq.heappush(heap, c)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)