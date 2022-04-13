class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        nums = {}
        for a, b in adjacentPairs:
            nums[a] = nums.get(a, []) + [b]
            nums[b] = nums.get(b, []) + [a]
        n = len(nums)
        op = []
        for num in nums:
            if len(nums[num]) == 1:
                op.extend([num, nums[num][0]])
                break
        while len(op) < n:
            prev = op[-1]
            prevprev = op[-2]
            op.extend([k for k in nums[prev] if k != prevprev])
        return op