class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        res = 0
        curr = 1
        blocked = set()
        for _ in range(n):
            while curr in blocked:
                curr += 1
            blocked.add(k - curr)
            res += curr
            curr += 1
        return res