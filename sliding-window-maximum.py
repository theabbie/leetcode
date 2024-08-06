from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque()
        res = []
        for i in range(n):
            while len(q) > 0 and q[0] <= i - k:
                q.popleft()
            while len(q) > 0 and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                if len(q) > 0:
                    res.append(nums[q[0]])
                else:
                    res.append(-1)
        return res