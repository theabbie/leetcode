class Solution:
    def checkPos(self, p, k, n):
        if k == 1:
            return True
        for i in range(n - k + 1):
            valid = True
            for b in range(32):
                if p[i + k][b] - p[i][b] > 1:
                    valid = False
                    break
            if valid:
                return True
        return False
    
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        beg = 1
        end = n
        res = 1
        p = [[0] * 32 for _ in range(n + 1)]
        for i in range(n):
            for b in range(32):
                p[i + 1][b] = p[i][b]
                if nums[i] & (1 << b):
                    p[i + 1][b] += 1
        while beg <= end:
            mid = (beg + end) // 2
            a = self.checkPos(p, mid, n)
            if a:
                beg = mid + 1
                res = mid
            else:
                end = mid - 1
        return res