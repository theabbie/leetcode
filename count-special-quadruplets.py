class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        ctr = 0
        exists = {}
        for i, num in enumerate(nums):
            exists[num] = exists.get(num, []) + [i]
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    val = nums[i] + nums[j] + nums[k]
                    if val in exists:
                        for p in exists[val]:
                            if p > k:
                                ctr += 1
        return ctr