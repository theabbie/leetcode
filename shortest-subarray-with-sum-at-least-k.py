class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + nums[i]
        res = n + 1
        i = 0
        parent = [-1] * (n + 1)
        def find(x):
            if parent[x] == -1:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        stack = []
        for j in range(n + 1):
            while stack and p[j] < p[stack[-1]]:
                curr = stack.pop()
                parent[curr] = find(j)
            stack.append(j)
            while i < j and p[j] - p[find(i + 1)] >= k:
                i += 1
            if p[j] - p[i] >= k:
                res = min(res, j - i)
        if res == n + 1:
            res = -1
        return res