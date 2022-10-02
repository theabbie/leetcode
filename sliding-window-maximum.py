from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        q = deque()
        for i in range(n):
            while len(q) > 0 and q[0] <= i - k:
                q.popleft()
            while len(q) > 0 and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res