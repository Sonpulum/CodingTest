import sys
n, x = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

if 0 != sum(arr):
    max_v = sum(arr[:x])
    e_v = max_v
    cnt = 1

    for i in range(1,n-x+1):
        e_v = e_v - arr[i-1] + arr[x-1+i]

        if e_v > max_v:
            cnt = 1
            max_v = e_v

        elif e_v == max_v:
            cnt += 1

    print(max_v)
    print(cnt)
    
else:
    print("SAD")