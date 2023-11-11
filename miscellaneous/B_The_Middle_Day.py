m = int(input())

d = list(map(int, input().split()))

x = (sum(d) + 1) // 2

i = 0

while i < len(d) and x - d[i] > 0:
    x -= d[i]
    i += 1

print(i + 1, x)