# 남학생은 자기가 받은 수의 배수 스위치들의 상태를 바꿈
# 여학생은 자기가 받은 수의 앞 뒤 스위치 상태를 비교하여 구간을 정한뒤 상태를 바꿈
# 여학생이 받은 수의 앞 뒤 스위치 상태가 같다면 2칸앞과 2칸뒤의 상태 비교 ...

import sys
n = int(sys.stdin.readline().strip())
s = [None]+list(map(int, sys.stdin.readline().split()))
c = int(sys.stdin.readline().strip())

def switch(num):
    if num == 0:
        return 1
    else:
        return 0
    
for _ in range(c):
    a, b = map(int, sys.stdin.readline().split())

    if a == 1:
        for i in range(b, n+1, b):
            s[i] = switch(s[i])
    
    else:
        s[b] = switch(s[b])
        ps = b-1
        pe = b+1
        while ps >= 1 and pe <= n:
            if s[ps] == s[pe]:
                s[ps] = switch(s[ps])
                s[pe] = switch(s[pe])
                ps -= 1
                pe += 1
            else:
                break

for i in range(1,n+1):
    print(s[i], end=' ')
    if i %20 == 0:
        print("")