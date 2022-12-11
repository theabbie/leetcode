class Solution:
    def possible(self, stones, n, x):
        i = 0
        v = set()
        prev = {}
        pj = 0
        for j in range(n):
            if stones[j] - stones[i] <= x and (j == n - 1 or stones[j + 1] - stones[i] > x):
                i = j
                if j != n - 1:
                    v.add(j)
            else:
                prev[j] = pj
                pj = j
        prev[n - 1] = pj
        if i != n - 1:
            return False
        i = n - 1
        for j in range(n - 1, -1, -1):
            if j not in v:
                if stones[i] - stones[j] <= x and (j == 0 or stones[i] - stones[prev[j]] > x):
                    i = j
        return i == 0
    
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)
        beg = 0
        end = 1
        while not self.possible(stones, n, end):
            end *= 2
        beg = end // 2
        res = end
        while beg <= end:
            mid = (beg + end) // 2
            if self.possible(stones, n, mid):
                res = mid
                end = mid - 1
            else:
                beg = mid + 1
        return res