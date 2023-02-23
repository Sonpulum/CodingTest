import sys
n = int(sys.stdin.readline().strip())
arr = sorted([int(sys.stdin.readline().strip()) for _ in range(n)],reverse=True)
c = n//3
result = sum(arr)

for i in range(1,c+1):
    result-=arr[i*3-1]

print(result)