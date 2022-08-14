t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    minyet = float('inf')
    reduced = set()
    for i in range(n - 1, -1, -1):
        if arr[i] in reduced:
            arr[i] = 0
        if arr[i] > minyet:
            reduced.add(arr[i])
        minyet = min(minyet, arr[i])
    minyet = float('inf')
    for i in range(n - 1, -1, -1):
        if arr[i] in reduced:
            arr[i] = 0
        if arr[i] > minyet:
            reduced.add(arr[i])
        minyet = min(minyet, arr[i])
    print(len(reduced))