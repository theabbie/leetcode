class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        s = 0
        res = 0
        for i in range(1, n + 1):
            if s + i <= maxSum and i not in banned:
                s += i
                res += 1
        return res