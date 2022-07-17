from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        pos = {}
        ctr = defaultdict(int)
        for i, el in enumerate(nums):
            ctr[el] += 1
            if el in pos:
                pos[el][1] = i
            else:
                pos[el] = [i, i]
        deg = max(ctr.values())
        return min(p[1] - p[0] + 1 for el, p in pos.items() if ctr[el] == deg)