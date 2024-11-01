class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        beg = min(nums)
        end = max(nums)
        while end - beg > 0.00001:
            mid = (beg + end) / 2
            p = [0] * (n + 1)
            for i in range(n):
                p[i + 1] = p[i] + nums[i] - mid
            sp = [float('inf')] * (n + 2)
            for i in range(n + 1):
                sp[i + 1] = min(sp[i], p[i])
            pos = False
            for j in range(k - 1, n + 1):
                if sp[j - k + 1] <= p[j]:
                    pos = True
                    break
            if pos:
                beg = mid
            else:
                end = mid
        return beg