t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    i = 0
    while i < n:
        ctr = 1
        curr = []
        while i < n - 1 and (arr[i] < 0) == (arr[i + 1] < 0):
            ctr += 1
            i += 1
            curr.append(arr[i])
        if arr[i] < 0:
            pass
        else:
            res += sum(curr) - sum(curr[:len(curr) // 2])
        i += 1