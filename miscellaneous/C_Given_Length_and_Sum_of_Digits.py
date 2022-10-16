n, s = map(int, input().split())

if s == 0:
    if n == 1:
        print(0, 0)
    else:
        print(-1, -1)
    exit(0)

small = [0] * n
small[0] = 1
big = [0] * n
big[0] = 1

s -= 1

if s > 9 * n - 1:
    print(-1, -1)
    exit(0)

smalls = s
for i in range(n - 1, -1, -1):
    diff = min(9 - small[i], smalls)
    small[i] += diff
    smalls -= diff

bigs = s
for i in range(n):
    diff = min(9 - big[i], bigs)
    big[i] += diff
    bigs -= diff

print("".join(map(str, small)), "".join(map(str, big)))