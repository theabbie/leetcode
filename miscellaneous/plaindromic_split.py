t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    i = 0
    j = n - 1
    while i + 1 < j:
        if arr[i] < arr[j]:
            arr[j] -= arr[i]
            res += 1
            i += 1
        elif arr[i] > arr[j]:
            arr[i] -= arr[j]
            res += 1
            j -= 1
        else:
            i += 1
            j -= 1
    if i + 1 == j and arr[i] != arr[j]:
        res += 1
    print(res)