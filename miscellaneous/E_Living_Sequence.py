from collections import defaultdict

t = int(input())

def count(num):
    num = str(num)
    n = len(num)
    prev = [1, 1]
    for i in range(n - 1, -1, -1):
        curr = [0, 0]
        for tight in range(2):
            maxdigit = 9
            if tight:
                maxdigit = int(num[i])
            if maxdigit == 4:
                curr[tight] += 4 * prev[0]
            elif maxdigit > 4:
                curr[tight] += (maxdigit - 1) * prev[0]
                curr[tight] += prev[tight]
            else:
                curr[tight] += maxdigit * prev[0]
                curr[tight] += prev[tight]
        prev = curr
    return prev[1]

for _ in range(t):
    k = int(input())
    beg = 1
    end = 1
    while count(end) < k + 1:
        end *= 2
    beg = end // 2
    res = -1
    while beg <= end:
        mid = (beg + end) // 2
        if count(mid) >= k + 1:
            res = mid
            end = mid - 1
        else:
            beg = mid + 1
    print(res)