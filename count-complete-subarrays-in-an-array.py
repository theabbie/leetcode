class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        pos = defaultdict(list)
        curr = 0
        for i in range(n - 1, -1, -1):
            pos[nums[i]].append(i)
        for el in pos:
            curr = max(curr, pos[el][-1])
        res = 0
        for i in range(n):
            res += n - curr
            pos[nums[i]].pop()
            curr = max(curr, n if len(pos[nums[i]]) == 0 else pos[nums[i]][-1])
        return res