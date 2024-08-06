class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        q = deque([(0, 0)])
        rmax = -1
        while q:
            i, d = q.pop()
            if i == n - 1:
                return d
            l = rmax + 1
            r = min(i + nums[i], n - 1)
            for j in range(l, r + 1):
                rmax = max(rmax, j)
                q.appendleft((j, d + 1))