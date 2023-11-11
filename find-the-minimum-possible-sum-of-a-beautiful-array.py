class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        curr = 1
        res = 0
        seen = set()
        for _ in range(n):
            while target - curr in seen:
                curr += 1
            seen.add(curr)
            res += curr
            curr += 1
        return res