from collections import defaultdict

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        ctr = defaultdict(int)
        for el in nums:
            if el % 2 == 0:
                ctr[el] += 1
        if len(ctr) == 0:
            return -1
        return -max((v, -k) for k, v in ctr.items())[1]