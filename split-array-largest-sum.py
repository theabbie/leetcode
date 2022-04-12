class Solution:
    def maxSum(self, prefix, i, j, m):
        if m == 1:
            return prefix[j] - prefix[i]
        key = (i, j, m)
        if key in self.cache:
            return self.cache[key]
        minVal = float('inf')
        for k in range(i + 1, j - m + 2):
            if prefix[k] - prefix[i] >= minVal:
                break
            val = max(prefix[k] - prefix[i], self.maxSum(prefix, k, j, m - 1))
            minVal = min(minVal, val)
        self.cache[key] = minVal
        return minVal
    
    def splitArray(self, nums: List[int], m: int) -> int:
        self.cache = {}
        n = len(nums)
        prefix = [0]
        for el in nums:
            prefix.append(prefix[-1] + el)
        return self.maxSum(prefix, 0, n, m)