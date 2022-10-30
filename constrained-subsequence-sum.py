from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = deque()
        for i in range(n):
            if len(q) > 0:
                nums[i] = max(nums[i], nums[i] + nums[q[0]])
            while len(q) > 0 and q[0] <= i - k:
                q.popleft()
            while len(q) > 0 and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
        return max(nums)