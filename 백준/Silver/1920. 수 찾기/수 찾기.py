import sys

n = int(input())
arr_a = list(map(int, sys.stdin.readline().split()))
arr_a.sort()

m = int(input())
arr_x = list(map(int, sys.stdin.readline().split()))

def binary(x):
    start = 0
    end = n-1
    
    while start <= end:
        mid = (start + end) // 2  # 중간값 갱신

        if arr_a[mid] == x:  # 찾으면 1 반환
            return 1
        elif arr_a[mid] > x:  # 찾는 값이 더 작으면 왼쪽 탐색
            end = mid - 1
        else:  # 찾는 값이 더 크면 오른쪽 탐색
            start = mid + 1

    return 0  # 찾지 못한 경우 0 반환

for i in arr_x:
    print(binary(i))