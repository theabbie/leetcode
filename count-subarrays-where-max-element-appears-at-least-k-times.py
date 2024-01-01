from sortedcontainers import SortedList

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        M = max(nums)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + int(nums[i] == M)
        res = 0
        bst = SortedList()
        for i in range(n + 1):
            res += bst.bisect_left(p[i] - k + 1)
            bst.add(p[i])
        return res