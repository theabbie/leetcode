class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        curr = 0
        prevsum = {}
        ctr = 0
        for num in nums:
            curr += num
            if curr == k:
                ctr += 1
            if (curr - k) in prevsum:
                ctr += prevsum[curr - k]
            prevsum[curr] = prevsum.get(curr, 0) + 1
        return ctr