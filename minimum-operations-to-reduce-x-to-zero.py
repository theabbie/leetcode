class Solution:
    def lenOfLongestSubarrayWithSum(self, arr, n, k):
        prevsums = {}
        total = 0
        maxLen = 0
        for i in range(n):
            total += arr[i]
            if (total == k):
                maxLen = i + 1
            elif (total - k) in prevsums:
                maxLen = max(maxLen, i - prevsums[total - k])
            if total not in prevsums:
                prevsums[total] = i
        return maxLen
    
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)
        if total == x:
            return n
        k = self.lenOfLongestSubarrayWithSum(nums, n, total - x)
        if k == 0:
            return -1
        return n - k