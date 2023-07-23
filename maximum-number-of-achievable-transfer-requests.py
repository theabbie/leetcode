class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)
        res = 0
        left = {}
        l, r = m // 2, m - m // 2
        for mask in range(1 << l):
            ctr = [0] * n
            x = 0
            for i in range(l):
                if mask & (1 << i):
                    ctr[requests[i][0]] -= 1
                    ctr[requests[i][1]] += 1
                    x += 1
            ctr = tuple(ctr)
            if x > left.get(ctr, float('-inf')):
                left[ctr] = x
        for mask in range(1 << r):
            ctr = [0] * n
            x = 0
            for i in range(r):
                if mask & (1 << i):
                    ctr[requests[l + i][0]] += 1
                    ctr[requests[l + i][1]] -= 1
                    x += 1
            ctr = tuple(ctr)
            res = max(res, left.get(ctr, float('-inf')) + x)
        return res