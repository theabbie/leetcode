t = int(input())

def sign(x):
    if x < 0:
        return -1
    return 1

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    newarr = []
    i = 0
    while i < n:
        ctr = 1
        while i < n - 1 and arr[i] == arr[i + 1]:
            ctr += 1
            i += 1
        newarr.append(arr[i])
        i += 1
    arr = newarr
    n = len(arr)
    i = 0
    while i < n:
        ctr = 1
        curr = sign(arr[i + 1] - arr[i]) if i < n - 1 else 1
        while i < n - 1 and sign(arr[i + 1] - arr[i]) == curr:
            ctr += 1
            i += 1
        res += 2
        if arr[i] == arr[i - ctr + 1]:
            res -= 1
        i += 1
    print(res)