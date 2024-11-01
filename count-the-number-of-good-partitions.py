class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        M = 10 ** 9 + 7
        r = -1
        l = {}
        for i, el in enumerate(nums):
            l[el] = i
        res = pow(2, M - 2, M)
        for i in range(len(nums)):
            if i > r:
                res *= 2
                res %= M
            r = max(r, l[nums[i]])
        return res