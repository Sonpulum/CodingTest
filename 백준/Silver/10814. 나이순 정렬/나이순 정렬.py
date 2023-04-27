import sys

n = int(sys.stdin.readline().strip())
arr = []

for i in range(n):
  a,b = map(str, sys.stdin.readline().split())
  arr.append([int(a),b,i])

arr.sort(key = lambda x : (x[0],x[2]))

for i in arr:
  print(i[0],i[1])