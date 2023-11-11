from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        nums = defaultdict(list)
        singles = set()
        for a, b in adjacentPairs:
            nums[a].append(b)
            nums[b].append(a)
            if a in singles:
                singles.remove(a)
            else:
                singles.add(a)
            if b in singles:
                singles.remove(b)
            else:
                singles.add(b)
        first = list(singles)[0]
        n = len(nums)
        res = []
        res.extend([first, nums[first][0]])
        while len(res) < n:
            prev = res[-1]
            prevprev = res[-2]
            res.extend([k for k in nums[prev] if k != prevprev])
        return res