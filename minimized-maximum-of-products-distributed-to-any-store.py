import math

class Solution:
    def isPossible(self, k, n, quantities):
        if k == 0:
            return False
        curr = 0
        for q in quantities:
            curr += math.ceil(q / k)
        return curr <= n
    
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        end = 1
        while not self.isPossible(end, n, quantities):
            end *= 2
        beg = end // 2
        res = end
        while beg <= end:
            mid = (beg + end) // 2
            if self.isPossible(mid, n, quantities):
                res = mid
                end = mid - 1
            else:
                beg = mid + 1
        return res