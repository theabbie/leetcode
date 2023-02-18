from collections import Counter

t = int(input())

def solve(a, b):
    if len(b) < len(a):
        a, b = b, a
    ctra = Counter(a)
    ctrb = Counter(b)
    for c in ctra:
        ctrb[c] -= ctra[c]
        if ctrb[c] < 0:
            return "NO"
    odd = 0
    for c in ctrb:
        if ctrb[c] & 1:
            odd += 1
    if odd > 1:
        return "NO"
    return "YES"

for _ in range(t):
    n, m = map(int, input().split())
    a = input()
    b = input()
    print(solve(a, b))