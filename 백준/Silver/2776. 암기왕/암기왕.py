import sys

t = int(sys.stdin.readline().strip())
ans = []
for _ in range(t):
  n = int(sys.stdin.readline().strip())
  note1 = sorted(list(map(int, sys.stdin.readline().split())))
  m = int(sys.stdin.readline().strip())
  note2 = list(map(int, sys.stdin.readline().split()))
  
  for i in note2:
    start = 0
    end = n-1
    flag = False
    while start <= end:
      mid = (start + end) // 2
      if note1[mid] > i:
        end = mid - 1
      elif note1[mid] < i:
        start = mid + 1
      else:
        flag = True
        break
    if(flag):
      ans.append(1)
    else:
      ans.append(0)

print(*ans, sep='\n')