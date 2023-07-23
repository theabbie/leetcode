from collections import Counter
import random

n = int(input())

arr = list(map(int, input().split()))

rands = random.sample(range(10 ** 9), n)

mp = {}

for i in range(n):
    mp[i + 1] = rands[i]

print(mp)

xorperm = [0] * n

xorperm[0] = mp[1]

for i in range(1, n):
    xorperm[i] = xorperm[i - 1] ^ mp[i + 1]

res = 0

for i in range(n):
    x = 0
    for j in range(n):
        x ^= mp[arr[j]]
        if x == xorperm[j - i]:
            res += 1

print(res)