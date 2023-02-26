import sys
import math
max_num = 1000000
prime_num = [False,False] + [True]*(max_num-1)
prime_arr = []
result = 1
for i in range(2,int(math.sqrt(max_num))+1):
    if prime_num[i]:
        for j in range(i*2, max_num+1, i):
            prime_num[j] = False

n = int(sys.stdin.readline().strip())
arr = list(set(map(int, sys.stdin.readline().split())))

for i in arr:
    if prime_num[i]:
        prime_arr.append(i)

if prime_arr:
    for i in prime_arr:
        result *= i
    print(result)

else:
    print(-1)