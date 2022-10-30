n, x, y = map(int, input().split())

arr = list(map(int, input().split()))

def isSubset(set, sum):
    n = len(set)
    if sum == 0:
        return True
    subset = ([[False for i in range(sum + 1)]
               for i in range(n + 1)])
    for i in range(n + 1):
        subset[i][0] = True
    for i in range(1, sum + 1):
        subset[0][i] = False
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j < set[i-1]:
                subset[i][j] = subset[i-1][j]
            if j >= set[i-1]:
                subset[i][j] = (subset[i-1][j] or
                                subset[i - 1][j-set[i-1]])
    return subset[n][sum]

sx = 0
sy = 0

for i in range(n):
    if i & 1:
        sy += arr[i]
    elif i > 0:
        sx += arr[i]

if (sy - y) & 1:
    print("No")
    exit(0)

if (sx - x + arr[0]) & 1:
    print("No")
    exit(0)

xarr = arr[2::2]
yarr = arr[1::2]

if isSubset(xarr, (sx - x + arr[0]) // 2) and isSubset(yarr, (sy - y) // 2):
    print("Yes")
else:
    print("No")