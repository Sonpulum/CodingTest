n, m = map(int, input().split())
cards = list(map(int, input().split()))
res = 0

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            total = cards[i] + cards[j] + cards[k]
            if total <= m:
                res = max(res,total)

print(res)