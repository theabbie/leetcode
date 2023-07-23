from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 4)

t = int(input())

def find(arr, val):
    beg = 0
    end = len(arr) - 1
    res = -1
    while beg <= end:
        mid = (beg + end) // 2
        if arr[mid] > val:
            res = arr[mid]
            end = mid - 1
        else:
            beg = mid + 1
    return res

for _ in range(t):
    s = list(map(int, list(input())))
    pos = defaultdict(list)
    for i in range(len(s)):
        pos[s[i]].append(i)
    m = int(input())
    l = list(map(int, list(input())))
    r = list(map(int, list(input())))
    prev = -1
    v = True
    for i in range(m):
        curr = prev
        for d in range(l[i], r[i] + 1):
            curr = max(curr, find(pos[d], prev))
        if curr <= prev:
            v = False
            break
        print(prev, curr)
        prev = curr
    print("YES" if v else "NO")