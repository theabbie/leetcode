from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    ctra = Counter(a)
    ctrb = Counter(b)
    res = 0
    for c in range(26):
        res = max(res, min(ctra[chr(ord('a') + c)], ctrb[chr(ord('a') + c)]))
    print(res)