t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    runs = 0
    for i in range(n):
        runs += arr[i]
        if runs == i + 1:
            res += 1
    print(res)