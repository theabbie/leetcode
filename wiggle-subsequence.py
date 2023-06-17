class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        inc = [1] * n
        dec = [1] * n
        for j in range(n):
            for i in range(j):
                if nums[j] > nums[i]:
                    inc[j] = max(inc[j], 1 + dec[i])
                if nums[j] < nums[i]:
                    dec[j] = max(dec[j], 1 + inc[i])
        return max(max(inc), max(dec))