money = int(input())
arr = list(map(int, input().split()))
j_cash = money
s_cash = money
j_stock = 0
s_stock = 0

for i in range(len(arr)):
    if j_cash >= arr[i]:
        n_stock = j_cash//arr[i]
        j_stock += n_stock
        j_cash = j_cash-(n_stock*arr[i])

    if i>=3:
        if arr[i-3] > arr[i-2] > arr[i-1] and s_cash >= arr[i]:
            n_stock = s_cash//arr[i]
            s_stock += n_stock
            s_cash = s_cash-(n_stock*arr[i])
        elif arr[i-3] < arr[i-2] < arr[i-1] and s_stock >= 1:
            s_cash += s_stock*arr[i]
            s_stock = 0

s_asset = s_cash + s_stock*arr[-1]
j_asset = j_cash + j_stock*arr[-1]

if s_asset > j_asset:
    print("TIMING")
elif s_asset < j_asset:
    print("BNP")
else:
    print("SAMESAME")