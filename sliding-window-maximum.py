class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        parent = [-1] * n
        def find(x):
            if parent[x] == -1:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        stack = []
        beg = 0
        for i in range(n):
            while len(stack) > 0 and nums[i] > nums[stack[-1]]:
                curr = stack.pop()
                parent[curr] = find(i)
            stack.append(i)
            while beg + k - 1 <= i:
                res.append(nums[find(beg)])
                beg += 1
        return res