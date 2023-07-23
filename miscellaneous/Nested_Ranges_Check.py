n = int(input())

ranges = []

for i in range(n):
    a, b = map(int, input().split())
    ranges.append((a, b, i))

ranges.sort(key = lambda p: (p[0], -p[1]))

contains = [0] * n
contained = [0] * n

maxend = float('-inf')
minend = float('inf')

for i in range(n):
    if ranges[i][1] <= maxend:
        contained[ranges[i][2]] = 1
    maxend = max(maxend, ranges[i][1])

for i in range(n - 1, -1, -1):
    if ranges[i][1] >= minend:
        contains[ranges[i][2]] = 1
    minend = min(minend, ranges[i][1])

print(*contains)
print(*contained)