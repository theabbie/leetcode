def getmax(arr, sumarr):
    n = len(arr)
    p = [0] * (n + 1)
    for i in range(n):
        p[i + 1] += p[i] + sumarr[i]
    stack = []
    next_smaller = [n] * n
    prev_smaller = [-1] * n
    for i in range(n):
        while len(stack) > 0 and arr[i] < arr[stack[-1]]:
            curr = stack.pop()
            next_smaller[curr] = i
        if len(stack) > 0:
            prev_smaller[i] = stack[-1]
        stack.append(i)
    res = 0
    for i in range(n):
        l = prev_smaller[i]
        r = next_smaller[i]
        res = max(res, (p[r] - p[l + 1]) * arr[i])
    return res

m, n = map(int, input().split())

board = []

for _ in range(m):
    board.append(list(map(int, input().split())))

res = 0

colsums = [[0] * (m + 1) for _ in range(n)]

for i in range(m):
    for j in range(n):
        colsums[j][i + 1] += colsums[j][i] + board[i][j]

for i in range(m):
    minarr = [float('inf')] * n
    for j in range(i, m):
        for x in range(n):
            minarr[x] = min(minarr[x], board[j][x])
        sumarr = [colsums[x][j + 1] - colsums[x][i] for x in range(n)]
        res = max(res, getmax(minarr, sumarr))

print(res)