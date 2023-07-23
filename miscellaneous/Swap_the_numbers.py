t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if k >= n:
        print(*arr)
        continue
    j = 0
    while j + k < n:
        j += 1
    i = n - 1
    while i - k >= 0:
        i -= 1
    if i + 1 <= j:
        arr.sort()
        print(*arr)
    else:
        curr = arr[:j] + arr[i+1:]
        curr.sort(reverse = True)
        res = [0] * n
        for x in range(n):
            if not j <= x <= i:
                res[x] = curr.pop()
            else:
                res[x] = arr[x]
        print(*res)