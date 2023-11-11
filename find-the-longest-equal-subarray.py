from collections import defaultdict

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pos = defaultdict(list)
        for i in range(n):
            pos[nums[i]].append(i)
        res = 1
        for el in pos:
            curr = pos[el]
            m = len(curr)
            i = 0
            dels = 0
            for j in range(m - 1):
                dels += curr[j + 1] - curr[j] - 1
                while i <= j and dels > k:
                    dels -= curr[i + 1] - curr[i] - 1
                    i += 1
                if dels <= k:
                    res = max(res, j - i + 2)
        return res