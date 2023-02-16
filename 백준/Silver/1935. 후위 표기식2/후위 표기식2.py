import sys
from collections import deque
n = int(sys.stdin.readline().strip())
s = list(sys.stdin.readline().strip())
d = {}
for i in range(n):
    d[chr(65+i)] = int(sys.stdin.readline().strip())

oper = '+-*/'
q = deque()

for i in s:
    if i not in oper:
        q.append(d[i])
    else:
        if i == '+':
            a = q.pop()
            b = q.pop()
            q.append(b+a)
        elif i == '-':
            a = q.pop()
            b = q.pop()
            q.append(b-a)
        elif i == '*':
            a = q.pop()
            b = q.pop()
            q.append(b*a)
        else:
            a = q.pop()
            b = q.pop()
            q.append(b/a)
    
print('{:0.2f}'.format(q[0]))