import sys
arr = list(map(str,sys.stdin.readline().rstrip().split('.')))
arr = [len(i) for i in arr]
result = []
able = True

for i in arr:
    res = ''
    while i > 0:
        if i%2 != 0:
            able = False
            break

        elif i%4 == 0:
            res = ('A'*i) + res
            i = 0
            break

        else:
            i -= 2
            res = res+('B'*2)

    if able:
        result.append(res)
    else:
        break

answer = ''
for i in range(len(result)):
    if result[i] != '':
        answer += result[i]

    if i != len(result)-1:
        answer += '.'

if able:
    print(answer)
else:
    print(-1)