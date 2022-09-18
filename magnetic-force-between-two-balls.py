class Solution:
    def isPossible(self, position, n, d, m):
        i = 0
        for j in range(n):
            if position[j] - position[i] >= d:
                i = j
                m -= 1
        return m <= 1
    
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        d = 1
        while self.isPossible(position, n, d, m):
            d = 2 * d
        beg = d // 2
        end = d
        res = beg
        while beg <= end:
            mid = (beg + end) // 2
            if self.isPossible(position, n, mid, m):
                res = mid
                beg = mid + 1
            else:
                end = mid - 1
        return res