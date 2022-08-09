from collections import defaultdict

n = int(input())
s = input()

ctr = defaultdict(int)

for i in range(n - 1):
    ctr[s[i:i+2]] += 1

print(max(ctr, key = lambda c: ctr[c]))