class Solution:
    def pivotInteger(self, n: int) -> int:
        p = n * (n + 1) // 2
        for i in range(n + 1):
            if i * (i + 1) == i + p:
                return i
        return -1