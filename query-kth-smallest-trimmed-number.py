class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        trims = [[] for _ in range(101)]
        l = max(len(el) for el in nums)
        for i in range(1, l + 1):
            for j in range(n):
                trims[i].append((int(nums[j][-i:]), j))
            trims[i].sort()
        res = []
        for k, trim in queries:
            res.append(trims[trim][k - 1][1])
        return res