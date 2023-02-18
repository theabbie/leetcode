class Solution:
    def possible(self, a, b, n):
        return b in a * n
    
    def repeatedStringMatch(self, a: str, b: str) -> int:
        end = 1
        while not self.possible(a, b, end):
            end *= 2
            if end > 2 and len(a) * end > len(b) * 3:
                return -1
        beg = end // 2
        res = end
        while beg <= end:
            mid = (beg + end) // 2
            if self.possible(a, b, mid):
                res = mid
                end = mid - 1
            else:
                beg = mid + 1
        return res