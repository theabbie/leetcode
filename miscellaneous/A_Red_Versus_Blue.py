import math

t = int(input())

for _ in range(t):
    n, r, b = map(int, input().split())
    for k in range(1, n):
        curr = "".join(["R" * k + "B"] * math.ceil(n / (k + 1)))[:n]
        if curr.count("R") == r and curr.count("B") == b:
            print(curr)
            break