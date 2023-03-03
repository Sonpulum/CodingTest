n = int(input())
dict = {}

for _ in range(n):
    a,b = map(str, input().split('.'))
    if b in dict:
        dict[b] += 1
    else:
        dict[b] = 1

for name, cnt in sorted(list(dict.items())):
    print(name,cnt)