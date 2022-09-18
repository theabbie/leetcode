from collections import defaultdict
from typing import Counter

t = int(input())

for tt in range(1, t + 1):
    print(f"Case #{tt}: ", end = "")
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if n > 2 * k:
        print("NO")
    else:
        pos = True
        ctr = Counter(arr)
        for el in ctr:
            if ctr[el] > 2:
                pos = False
                break
        if pos:
            print("YES")
        else:
            print("NO")