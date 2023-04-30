import sys
m = int(sys.stdin.readline().strip())
s = []

for _ in range(m):
    cmd = list(map(str, sys.stdin.readline().split()))

    if cmd[0] == 'add':
        a = int(cmd[1])
        if a not in s:
            s.append(a)

    elif cmd[0] == 'remove':
        a = int(cmd[1])
        if a in s:
            s.remove(a)

    elif cmd[0] == 'check':
        a = int(cmd[1])
        if a in s:
            print(1)
        else:
            print(0)

    elif cmd[0] == 'toggle':
        a = int(cmd[1])
        if a not in s:
            s.append(a)
        else:
            s.remove(a)

    elif cmd[0] == 'all':
        s = [i for i in range(1,21)]

    else:
        s = []