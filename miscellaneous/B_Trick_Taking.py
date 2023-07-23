n, t = map(int, input().split())

c = list(map(int, input().split()))

r = list(map(int, input().split()))

pos = (-1, -1)

greatest = (-1, -1)

for i in range(n):
    if c[i] == t:
        pos = max(pos, (r[i], i))
    if c[i] == c[0]:
        greatest = max(greatest, (r[i], i))

if pos[1] == -1:
    pos = greatest

print(pos[1] + 1)