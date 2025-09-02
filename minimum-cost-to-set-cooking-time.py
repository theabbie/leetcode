v = {}

for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                m = 10 * i + j
                s = 10 * k + l
                sec = 60 * m + s
                if sec not in v:
                    v[sec] = []
                arr = [i, j, k, l]
                while arr and arr[0] == 0:
                    arr.pop(0)
                v[sec].append(arr)

class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        res = float('inf')
        for pos in v[targetSeconds]:
            curr = 0
            prev = startAt
            for btn in pos:
                if btn != prev:
                    curr += moveCost
                curr += pushCost
                prev = btn
            res = min(res, curr)
        return res