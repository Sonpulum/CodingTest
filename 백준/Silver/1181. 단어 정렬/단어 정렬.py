n = int(input())
arr = []

for i in range(n):
    s = input()
    e = [s,len(s)]
    if e not in arr:
        arr.append(e)

arr.sort(key = lambda x : (x[1],x[0]))
for i in arr:
    print(i[0])