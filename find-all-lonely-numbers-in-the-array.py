from collections import Counter

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        numctr = Counter(nums)
        op = []
        for num in nums:
            if numctr[num] == 1 and num - 1 not in numctr and num + 1 not in numctr:
                op.append(num)
        return op