import heapq
import sys
heap = []
result = []
n = int(sys.stdin.readline().strip())

for _ in range(n):
    s = int(sys.stdin.readline().strip())

    if s == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,-s)