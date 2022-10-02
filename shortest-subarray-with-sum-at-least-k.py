from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p = [0]
        for el in nums:
            p.append(p[-1] + el)
        q = deque()
        res = n + 1
        for i in range(n + 1):
            while len(q) > 0 and p[i] <= p[q[-1]]:
                q.pop()
            while len(q) > 0 and p[i] - p[q[0]] >= k:
                res = min(res, i - q.popleft())
            q.append(i)
        if res > n:
            return -1
        return res