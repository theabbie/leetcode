t = int(input())

def solve(n):
    i = 2
    while i * i < n:
        if n % i == 0:
            return [1, i, n // i]
        i += 1
    return [-1]

for _ in range(t):
    n = int(input())
    print(*solve(n))