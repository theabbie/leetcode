from collections import deque, defaultdict

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dist = defaultdict(lambda: float('inf'))
        dist[0] = 0
        q = deque([0])
        while len(q) > 0:
            i = q.pop()
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                if dist[j] > dist[i] + 1:
                    dist[j] = dist[i] + 1
                    q.appendleft(j)
        return dist[n - 1]