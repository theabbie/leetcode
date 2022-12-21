class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        l = {}
        for el in nums:
            if el * el in l:
                l[el] = l[el * el] + 1
            else:
                l[el] = 1
        res = max(l.values())
        if res < 2:
            return -1
        return res