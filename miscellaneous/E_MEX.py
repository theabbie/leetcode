from collections import defaultdict, Counter

n = int(input())

arr = list(map(int, input().split()))

s = input()

left = defaultdict(lambda: Counter())

right = defaultdict(lambda: Counter())

for i in range(n):
    right[s[i]][arr[i]] += 1

res = 0

for i in range(n):
    left[s[i]][arr[i]] += 1
    right[s[i]][arr[i]] -= 1
    leftm = left["M"]
    rightx = right["X"]
    if s[i] != "E":
        continue
    for x in range(3):
        for y in range(3):
            mset = set([x, y, arr[i]])
            mex = 0
            while mex in mset:
                mex += 1
            res += mex * leftm[x] * rightx[y]

print(res)