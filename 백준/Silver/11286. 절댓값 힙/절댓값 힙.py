import heapq
import sys

heap = []
n = int(sys.stdin.readline().strip())

for _ in range(n):
    c = int(sys.stdin.readline().strip())
    if c == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap,[abs(c),c])