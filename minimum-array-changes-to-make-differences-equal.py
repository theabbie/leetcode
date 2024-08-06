from collections import Counter

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ops = []
        ctr = Counter()
        for i in range(n // 2):
            a, b = nums[i], nums[n - i - 1]
            a, b = min(a, b), max(a, b)
            maxdiff = max(b, k - a)
            ops.append(maxdiff)
            ctr[b - a] += 1
        ops.sort(reverse = True)
        res = float('inf')
        i = 0
        for diff in range(k, -1, -1):
            while i < len(ops) and ops[i] >= diff:
                i += 1
            res = min(res, i + 2 * (len(ops) - i) - ctr[diff])
        return res