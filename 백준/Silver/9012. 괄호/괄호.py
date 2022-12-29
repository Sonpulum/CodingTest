import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    s = sys.stdin.readline().strip()
    while '()' in s:
        s = s.replace('()','')
    if len(s) == 0:
        print('YES')
    else:
        print('NO')