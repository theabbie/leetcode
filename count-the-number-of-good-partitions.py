class Solution:
    def merge(self, intervals):
        n = len(intervals)
        intervals.sort()
        prev = float('-inf')
        res = []
        for a, b in intervals:
            if a > prev:
                res.append([a, b])
            else:
                res[-1][1] = max(res[-1][1], b)
            prev = max(prev, b)
        return res
    
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        inv = []
        f = {}
        l = {}
        for i in range(n):
            if nums[i] not in f:
                f[nums[i]] = i
            l[nums[i]] = i
        for el in f:
            inv.append((f[el], l[el]))
        return pow(2, len(self.merge(inv)) - 1, 10 ** 9 + 7)