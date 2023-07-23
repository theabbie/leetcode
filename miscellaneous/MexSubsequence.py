from collections import defaultdict
import random

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

s = list("0123456789" * 50)

random.shuffle(s)

# print("".join(s))

n = len(s)

pos = defaultdict(list)

for i in range(n):
    pos[s[i]].append(i)
    
def count(num, i, n, tight, zero, prev, cache):
    if not zero and prev == -1:
        return 0
    if i >= n:
        return 1
    key = (i, tight, zero, prev)
    if key in cache:
        return cache[key]
    maxd = 9
    if tight:
        maxd = int(num[i])
    res = 0
    for d in range(maxd + 1):
        currzero = zero and d == 0
        j = prev
        if not currzero:
            j = find(pos[str(d)], prev)
        res += count(num, i + 1, n, tight and d == maxd, currzero, j, cache)
    cache[key] = res
    return res

end = 1
while count(str(end), 0, len(str(end)), True, True, -1, {}) == end + 1:
    end *= 2

beg = end // 2
res = -1

while beg <= end:
    mid = (beg + end) // 2
    if count(str(mid), 0, len(str(mid)), True, True, -1, {}) == mid + 1:
        beg = mid + 1
    else:
        res = mid
        end = mid - 1

print(res)

# for i in range(res + 1):
#     curr = str(i)
#     m = len(curr)
#     k = 0
#     for j in range(n):
#         if k < m and s[j] == curr[k]:
#             k += 1
#     print(i, k == m)