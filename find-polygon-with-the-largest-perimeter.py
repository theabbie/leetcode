class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        s = c = 0
        res = -1
        for el in nums:
            if c >= 2 and s > el:
                res = max(res, s + el)
            s += el
            c += 1
        return res