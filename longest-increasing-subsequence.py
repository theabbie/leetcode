import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for el in nums:
            x = bisect.bisect_left(res, el)
            if x < len(res):
                res[x] = el
            else:
                res.append(el)
        return len(res)