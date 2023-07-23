t = int(input())

def solve(n, x):
    for a in range(n + 1):
        s = n - a
        d = x - 1
        if (s + d) % 2 == 0 and (s - d) % 2 == 0 and 0 <= (s + d) // 2 <= n and 0 <= (s - d) // 2 <= n:
            b = (s + d) // 2
            c = (s - d) // 2
            return "*" * a + "+" * b + "-" * c
    return -1

for _ in range(t):
    n, x = map(int, input().split())
    print(solve(n, x))