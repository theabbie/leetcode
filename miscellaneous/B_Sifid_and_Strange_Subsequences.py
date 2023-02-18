t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    diffs = []
    for i in range(n - 1):
        diffs.append(arr[i + 1] - arr[i])
    print(diffs)