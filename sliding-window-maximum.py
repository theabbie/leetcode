class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        parent = [-1] * len(nums)
        def find(x):
            if parent[x] == -1:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        stack = []
        for i, el in enumerate(nums):
            while stack and el > nums[stack[-1]]:
                curr = stack.pop()
                parent[curr] = find(i)
            stack.append(i)
            if i >= k - 1:
                res.append(nums[find(i - k + 1)])
        return res