m, n = map(int, input().split())

ctr = [0] * n

for _ in range(m):
    s = input()
    for i in range(n):
        if s[i] == "#":
            ctr[i] += 1

print(*ctr)