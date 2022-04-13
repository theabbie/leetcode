class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        nums = {}
        singles = set()
        for a, b in adjacentPairs:
            nums[a] = nums.get(a, []) + [b]
            nums[b] = nums.get(b, []) + [a]
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
        op = []
        op.extend([first, nums[first][0]])
        while len(op) < n:
            prev = op[-1]
            prevprev = op[-2]
            op.extend([k for k in nums[prev] if k != prevprev])
        return op