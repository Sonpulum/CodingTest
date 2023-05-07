n = int(input())
a = [int(input()) for _ in range(n)]

a_max = max(a)
cnt = 0

while True:
    if a[0] != a_max:
        a[a.index(a_max)] -= 1
        a[0] += 1
        a_max = max(a)
        cnt += 1

    else:
        if a.count(a_max) > 1:
            for i in range(1,n):
                if a[i] == a_max:
                    a[i] -= 1
                    a[0] += 1
                    a_max = max(a)
                    cnt += 1
                    break
        else:
            break

print(cnt)