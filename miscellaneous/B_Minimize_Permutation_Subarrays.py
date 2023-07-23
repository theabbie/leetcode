t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    pos = {}
    for i in range(n):
        pos[arr[i]] = i
    minpos = n
    maxpos = -1
    for i in range(1, n + 1):
        minpos = min(minpos, pos[i])
        maxpos = max(maxpos, pos[i])
        if maxpos - minpos + 1 == i and minpos <= pos[1] <= maxpos: