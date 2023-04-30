import sys
n = int(sys.stdin.readline().strip())
id_dict = {}
cnt = 0

for _ in range(n):
    s = sys.stdin.readline().strip()
    
    if s == 'ENTER':
        id_dict = {}

    else:
        if s not in id_dict:
            id_dict[s] = 1
            cnt += 1

print(cnt)