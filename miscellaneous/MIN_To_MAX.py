from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    M = min(arr)
    print(n - Counter(arr)[M])