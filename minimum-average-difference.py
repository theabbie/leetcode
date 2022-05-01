class Solution:
    def getDiff(self, prefix, i, n):
        l = (prefix[i + 1] - prefix[0])
        r = prefix[-1] - l
        l = l // (i + 1)
        r = r // (n - i - 1) if i < n - 1 else 0
        return abs(l - r)
    
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1] + nums[i])
        return min(range(n), key = lambda i: self.getDiff(prefix, i, n))