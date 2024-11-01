class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        total = sum(nums)
        res = total
        vals = [(el ^ k, el) for el in nums]
        vals.sort(key = lambda x: x[1] - x[0])
        p = 0
        for i in range(len(nums)):
            p += vals[i][0]
            total -= vals[i][1]
            if i & 1:
                res = max(res, p + total)
        return res