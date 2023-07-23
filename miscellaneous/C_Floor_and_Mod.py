t = int(input())

def solve(x, y):
    res = 0
    i = 0
    for i in range(2, min(x, y + 1) + 1):
        j = 1
        while i * j <= x:
            if j == (i * j) // (i - 1):
                res += 1
            j += 1
    return res

for _ in range(t):
    x, y = map(int, input().split())
    print(solve(x, y))