class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        mydict = {}
        total = 0
        maxLen = 0
        for i in range(n):
            total += arr[i]
            if (total == k):
                maxLen = i + 1
            elif (total - k) in mydict:
                maxLen = max(maxLen, i - mydict[total - k])
            if total not in mydict:
                mydict[total] = i
        return maxLen
    
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)
        if total == x:
            return n
        if total < x:
            return -1
        k = self.lenOfLongSubarr(nums, n, total - x)
        return n - k if k > 0 else -1