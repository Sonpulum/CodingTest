import sys

n, k = map(int, sys.stdin.readline().split())
prime = [False,False] + [True]*(n-1)
cnt = 0
result = 0

for i in range(2,n+1):
    if prime[i]:
        cnt += 1
        if cnt == k:
            result = i
            break

        for j in range(i*2, n+1, i):
            if prime[j]:
                prime[j] = False
                cnt += 1
                if cnt == k:
                    result = j
                    break
    
    if result != 0:
        break

print(result)