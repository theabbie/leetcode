from collections import Counter

M = 998244353

n = int(input())

cards = []

for _ in range(n):
    a, b = map(int, input().split())
    cards.append((a, b))

res = pow(2, n, M)

front = Counter()
back = Counter()

for i in range(n):
    front[cards[i][0]] += 1
    back[cards[i][1]] += 1

curr = 0

for el in front:
    if front[el] >= 2:
        curr -= pow(2, front[el] - 2, M)
        curr %= M

for el in back:
    if back[el] >= 2:
        curr += pow(2, back[el] - 2, M)
        curr %= M

print((M + res - curr) % M)