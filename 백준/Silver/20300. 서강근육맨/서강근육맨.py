import sys
n = int(sys.stdin.readline().strip())
l = sorted(list(map(int, sys.stdin.readline().split())))
m_arr = []

if n%2 == 0:
    for i in range(n//2):
        m_arr.append(l[i]+l[n-i-1])

else:
    for i in range(n//2):
        m_arr.append(l[i]+l[n-i-2])
    m_arr.append(l[-1])

print(max(m_arr))