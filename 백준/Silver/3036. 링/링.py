import sys
n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().split()))
ans = []

def lcm(a,b):
    while b > 0:
        a = a % b
        a,b = b,a

    return(a)

for i in range(1,n):
    r = lcm(a[0],a[i])
    print(str(a[0]//r)+'/'+str(a[i]//r))