class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if k > min(nums):
            return -1
        return len(set(x for x in nums if x > k))