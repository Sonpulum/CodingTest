import sys
score = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

total = 0
cnt = 0

for i in range(20):
    n, t, g = map(str, sys.stdin.readline().split())
    if g != 'P':
        total += (score[g] * float(t))
        cnt += float(t)

answer = round(total/cnt,6)
print(answer)