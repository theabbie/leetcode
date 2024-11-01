class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        res = {}
        n = len(nums)
        stack = []
        nxt = [n] * n
        prv = [-1] * n
        for i in range(n):
            while len(stack) > 0 and nums[i] > nums[stack[-1]]:
                curr = stack.pop()
                nxt[curr] = i
            if len(stack) > 0:
                prv[i] = stack[-1]
            stack.append(i)
        for i in range(n):
            res[nums[i]] = max(res.get(nums[i], 1), nxt[i] - prv[i] - 1)
        return [res[el] for el in nums]