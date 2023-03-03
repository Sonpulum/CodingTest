board = [list(map(int, input().split())) for _ in range(5)]
board_reverse = [[0 for _ in range(5)] for _ in range(5)]
cross =[[0 for _ in range(5)] for _ in range(2)]

def check(arr, num):
    for i in range(5):
        if arr[i] == num:
            arr[i] = 0
    return arr

for i in range(5):
    for j in range(5):
        board_reverse[i][j] = board[j][i]
        if i == j:
            cross[0][i] = board[j][i]
        if i == 4-j:
            cross[1][i] = board[j][i]

remove_num = []

for _ in range(5):
    num_arr = list(map(int, input().split()))
    remove_num += num_arr

for i in range(25):
    bingo = 0

    for j in range(5):
        if remove_num[i] in board[j]:
            check(board[j],remove_num[i])
        if remove_num[i] in board_reverse[j]:
            check(board_reverse[j],remove_num[i])

    for k in range(2):
        if remove_num[i] in cross[k]:
            check(cross[k],remove_num[i])

    for j in range(5):
        if sum(board[j]) == 0:
            bingo += 1
        if sum(board_reverse[j]) == 0:
            bingo += 1

    for k in range(2):        
        if sum(cross[k]) == 0:
            bingo += 1

    if bingo >= 3:
        print(i+1)
        break