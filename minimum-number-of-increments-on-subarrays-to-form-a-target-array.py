class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        res = 0
        for i in range(n):
            prev = 0
            if i > 0:
                prev = target[i - 1]
            res += max(target[i] - prev, 0)
        return res