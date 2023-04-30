import sys
n = int(sys.stdin.readline().strip())
empl = {}
for _ in range(n):
    n, a = map(str, sys.stdin.readline().split())
    
    if a == 'enter':
        empl[n] = 1
    else:
        empl[n] = 0

empl_arr = []
for k, v in empl.items():
    if v == 1:
        empl_arr.append(k)

for i in sorted(empl_arr, reverse=True):
    print(i)