class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        p = [0]
        for num in nums:
            p.append(p[-1] + num)
        ctr = 0
        for i in range(n - 1):
            l = p[i + 1]
            r = p[-1] - l
            if l >= r:
                ctr += 1
        return ctr