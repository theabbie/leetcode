class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        have = Counter()
        for el in nums:
            have[(value + (el % value)) % value] += 1
        mex = 0
        while True:
            if have[mex % value] == 0:
                return mex
            have[mex % value] -= 1
            mex += 1