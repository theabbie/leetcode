from collections import Counter, defaultdict

t = int(input())

pals = set()

for i in range(10):
    pals.add(i)

for l in range(2, 6, 2):
    for i in range(10 ** (l // 2)):
        pals.add(int(str(i) + str(i)[::-1]))

for l in range(3, 6, 2):
    for i in range(1, 10 ** ((l - 1) // 2)):
        for j in range(10):
            pals.add(int(str(i) + str(j) + str(i)[::-1]))

pals = sorted(pals)

maxnum = pow(2, 15)

xorcounts = defaultdict(set)

for el in range(maxnum):
    for p in pals:
        xorcounts[el].add(el ^ p)
    xorcounts[el] = sorted(xorcounts[el])

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    M = max(arr)
    res = n
    ctr = Counter()
    for el in arr:
        for val in xorcounts[el]:
            if val > M:
                break
            res += ctr[val]
        ctr[el] += 1
    print(res)