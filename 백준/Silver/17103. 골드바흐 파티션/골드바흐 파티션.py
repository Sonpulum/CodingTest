import sys

max_num = 1000000
is_prime = [False,False] + [True] * (max_num -1)

for i in range(2,round(max_num**0.5 + 1)):
    if is_prime[i] == True:
        for j in range(i*2,max_num, i):
            is_prime[j] = False

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    cnt = 0

    for i in range(n//2+1):
        if is_prime[i] and is_prime[n-i]:
            cnt += 1

    print(cnt)