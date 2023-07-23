from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    grid = [a, b]
    ctr = Counter(a + b)
    absent = [i for i in range(2 * n + 1) if i not in ctr]
    if n & 1:
        i = 0
        while i in ctr:
            i += 1
        print(i)
    else:
        M = float('-inf')
        for i in range(n):
            if i % 2 == 0:
                if ctr[grid[1][i]] == 1:
                    if len(grid) == 0 or grid[1][i] < absent[0]:
                        M = max(M, grid[1][i])
                elif len(absent) > 0:
                    M = max(M, absent[0])
            else:
                if ctr[grid[0][i]] == 1:
                    if len(grid) == 0 or grid[0][i] < absent[0]:
                        M = max(M, grid[0][i])
                elif len(absent) > 0:
                    M = max(M, absent[0])
        print(M if M != float('-inf') else 2 * n + 1)