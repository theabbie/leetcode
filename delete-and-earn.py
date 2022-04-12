from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        prev = curr = 0
        for num in range(10001):
            prev, curr = curr, max(prev + num * ctr[num], curr)
        return curr