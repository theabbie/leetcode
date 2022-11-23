from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ctr = Counter(arr)
    valid = True
    for el in ctr:
        if ctr[el] > 2:
            valid = False
    print("Yes" if valid else "No")