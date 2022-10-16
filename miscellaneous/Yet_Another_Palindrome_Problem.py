t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    pos = True
    inc = []
    res = 0
    for i in range(n // 2):
        if arr[i] > arr[n - i - 1]:
            pos = False
        else:
            inc.append(arr[n - i - 1] - arr[i])
            res = max(res, arr[n - i - 1] - arr[i])
    if not pos or inc != sorted(inc, reverse = True):
        print(-1)
    else:
        print(res)