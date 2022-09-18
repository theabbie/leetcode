class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse = True)
        res = 0
        prev, ctr = None, 0
        for i in range(n):
            if prev == None:
                prev, ctr = nums[i], 1
            elif nums[i] == prev:
                ctr += 1
            else:
                res += ctr
                prev = nums[i]
                ctr += 1
        return res