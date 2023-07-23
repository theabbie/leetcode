t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print(1)
        continue
    res = []
    pos = {}
    for i in range(n):
        pos[arr[i]] = i
    r = pos[n]
    if r == 0:
        r = pos[n - 1]
    res.extend(arr[r:])
    if r == n - 1 and arr[r - 1] < arr[0]:
        res.extend(arr[:r])
        print(*res)
        continue
    if r > 0:
        l = r - 2
        while l > 0 and arr[l] > arr[0]:
            l -= 1
        l += 1
        res.extend(arr[l:r][::-1])
        res.extend(arr[:l])
    print(*res)