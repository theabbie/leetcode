from collections import Counter

n = int(input())

M = 10 ** 9 + 7

facts = [1] * (n + 1)

for i in range(1, n + 1):
    facts[i] = i * facts[i - 1]
    facts[i] %= M

ctr = Counter()

for _ in range(n):
    a, b = map(int, input().split())
    ctr[a] += 1

res = pow(facts[n], M - 2, M)

for el in ctr:
    res *= facts[ctr[el]]
    res %= M

print(res)