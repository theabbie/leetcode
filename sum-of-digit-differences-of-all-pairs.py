class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        while nums[0]:
            res += n * n
            ctr = [0] * 10
            for i in range(n):
                d = nums[i] % 10
                res -= 2 * ctr[d] + 1
                ctr[d] += 1
                nums[i] //= 10
        return res // 2