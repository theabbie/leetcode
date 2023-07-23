t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = [0] * n
    for i in range(n - 2):
        if max(res[i], res[i + 1]) != arr[i]:
            if res[i] == 0 and max(arr[i], res[i + 1]) == arr[i] and (i == 0 or max(res[i - 1], arr[i]) == arr[i - 1]):
                res[i] = arr[i]
            else:
                res[i + 1] = arr[i]
    res[-1] = arr[-1]
    print(*res)