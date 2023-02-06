n = input()
card1 = list(map(int, input().split()))
m = input()
card2 = list(map(int, input().split()))
cnt_dict = {}
result = []
for i in card1:
    if i in cnt_dict:
        cnt_dict[i] += 1
    else:
        cnt_dict[i] = 1

for j in card2:
    if j in cnt_dict:
        result.append(cnt_dict[j])
    else:
        result.append(0)

print(*result, end=' ')