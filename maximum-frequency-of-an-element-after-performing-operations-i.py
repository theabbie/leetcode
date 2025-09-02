import bisect

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        ctr = Counter(nums)
        s = set()
        for el in nums:
            s.add(el)
            s.add(el - k)
            s.add(el + k)
        res = 0
        for el in s:
            res = max(res, ctr[el] + min(bisect.bisect_right(nums, el + k) - bisect.bisect_left(nums, el - k) - ctr[el], numOperations))
        return res