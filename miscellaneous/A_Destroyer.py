from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    M = max(arr)
    ctr = Counter(arr)
    pos = True
    for i in range(M):
        if ctr[i] < ctr[i + 1]:
            pos = False
            break
    print("YES" if pos else "NO")