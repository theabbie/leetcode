t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if arr == arr[::-1]:
        print(0)
        continue
    pos = set()
    res = 1
    for i in range(n):
        if arr[i] != arr[n - i - 1]:
            pos.add(abs(arr[i] - arr[n - i - 1]))
    for p in pos:
        valid = True
        for i in range(n // 2):
            if arr[i] % p != arr[n - i - 1] % p:
                valid = False
                break
        if valid:
            res = max(res, p)
    print(max(pos))