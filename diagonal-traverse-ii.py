from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        diags = defaultdict(list)
        for i in range(m):
            n = len(nums[i])
            for j in range(n):
                diags[i + j].append((j, nums[i][j]))
        res = []
        for i in sorted(diags.keys()):
            res.extend([j[1] for j in sorted(diags[i])])
        return res