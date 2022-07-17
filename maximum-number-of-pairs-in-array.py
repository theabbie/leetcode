from collections import Counter

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        ctr = Counter(nums)
        res = [0, 0]
        for el in ctr:
            res[0] += ctr[el] // 2
            res[1] += ctr[el] % 2
        return res