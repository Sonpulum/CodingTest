import sys
def input():
  return sys.stdin.readline()

t = int(input().strip())

for _ in range(t):
  n = int(input().strip())
  arr = list(map(int, input().split()))
  print(min(arr),max(arr))