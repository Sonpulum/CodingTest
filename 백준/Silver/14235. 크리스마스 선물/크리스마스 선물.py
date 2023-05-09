import heapq
import sys
n = int(sys.stdin.readline().strip())
heap = []
for i in range(n):
  a = list(map(int, sys.stdin.readline().split()))
  if a[0] != 0:
    for j in a[1:]:
      heapq.heappush(heap,-j)
  else:
    if heap:
      print(-heapq.heappop(heap))
    else:
      print(-1)