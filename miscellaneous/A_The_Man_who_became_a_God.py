t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    diffs = []
    arr = list(map(int, input().split()))
    for i in range(n - 1):
        diffs.append(abs(arr[i + 1] - arr[i]))
    diffs.sort()
    for _ in range(k - 1):
        if len(diffs) > 0:
            diffs.pop()
    print(sum(diffs))