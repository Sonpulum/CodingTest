import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

def binary(s, e):
    start = s
    end = e
    ans = 0

    while start <= end:
        mid = (start + end) // 2  # 수정된 중간값 계산
        res = 0
        
        for tree in trees:
            if tree > mid:  # mid보다 큰 나무만 자름
                res += (tree - mid)

        if res >= m:
            ans = mid  # 적절한 높이를 갱신
            start = mid + 1
        else:
            end = mid - 1

    return ans

print(binary(0, max(trees)))