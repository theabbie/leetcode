t = int(input())

for _ in range(t):
    n = int(input())
    arr = sorted(map(int, input().split()))
    i = 0
    j = n - 1
    res = 0
    while i < j:
        res += arr[j] - arr[i]
        j -= 1
        i += 1
    print(res)