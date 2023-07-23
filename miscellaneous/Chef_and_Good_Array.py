from collections import Counter

t = int(input())

def checksum(arr, s):
    n = len(arr)
    right = {}
    pos = [float('inf')] * n
    for i in range(n - 1, -1, -1):
        if s - arr[i] in right:
            pos[i] = right[s - arr[i]]
        right[arr[i]] = i
    prev = n
    deletions = 0
    for i in range(n - 1, -1, -1):
        if pos[i] < prev:
            deletions += prev - pos[i] - 1
            deletions += pos[i] - i - 1
            prev = i
    deletions += prev
    return deletions

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ctr = Counter()
    for i in range(n):
        for j in range(i + 1, n):
            ctr[arr[j] - arr[i]] += 1
    res = n
    for el in ctr:
        if ctr[el] == ctr[-el]:
            res = min(res, n - ctr[el])
    print(res)