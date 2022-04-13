class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ctr = 0
        odd = 0
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[odd] += 1
            if nums[i] & 1:
                odd += 1
            if odd >= k:
                ctr += prefix[odd - k]
        return ctr