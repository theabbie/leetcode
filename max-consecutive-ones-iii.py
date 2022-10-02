class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p = [0]
        for el in nums:
            p.append(p[-1] + el)
        res = 0
        i = 0
        zeroes = lambda x, y: y - x + 1 - p[y + 1] + p[x]
        for j in range(n):
            while i < j and zeroes(i, j) > k:
                i += 1
            if zeroes(i, j) <= k:
                res = max(res, j - i + 1)
        return res