from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + nums[i]
        q = deque()
        res = n + 1
        i = 0
        for j in range(n + 1):
            while q and p[q[-1]] > p[j]:
                q.pop()
            q.append(j)
            while len(q) > 1 and p[j] - p[q[1]] >= k:
                q.popleft()
            if q and p[j] - p[q[0]] >= k:
                res = min(res, j - q[0])
        if res == n + 1:
            res = -1
        return res