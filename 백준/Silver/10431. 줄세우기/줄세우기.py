import sys

p = int(input())
ans = []
for i in range(p):
    t = list(map(int, sys.stdin.readline().split()))
    student = t[1:]
    cnt = 0

    calc = 0
    while(calc <= 19):
        if calc == 0:
            calc += 1
            
        if student[calc] < student[calc-1]:
            cnt += 1
            tmp = student[calc]
            student[calc] = student[calc-1]
            student[calc-1] = tmp
            calc -= 1

        else:
            calc += 1

    ans.append([t[0], cnt])

for i in ans:
    print(*i)