import sys

def gcd(a,b):
    while b!= 0:
        a = a%b
        a,b = b,a
    return a

t = int(sys.stdin.readline().strip())

for _ in range(t):
    result = 0
    arr = list(map(int, sys.stdin.readline().split()))
    n = arr[0]

    for i in range(1,n):
        for j in range(i+1,n+1):
            result += gcd(arr[i],arr[j])

    print(result)