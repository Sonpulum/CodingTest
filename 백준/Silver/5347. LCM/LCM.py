import sys
n = int(sys.stdin.readline().strip())

for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    mult = a*b

    while b!= 0:
        a = a%b
        a,b = b,a

    print(mult//a)