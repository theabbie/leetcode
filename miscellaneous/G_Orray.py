from functools import cmp_to_key

t = int(input())

def cmp(a, b):
    swap = False
    for x in range(32):
        if (a & (1 << x)) ^ (b & (1 << x)):
            swap = True
            break
    if swap:
        return -1
    return 1

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(key = cmp_to_key(cmp))
    print(*arr)