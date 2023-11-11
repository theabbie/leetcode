class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        a = b = 0
        for i in range(1, n + 1):
            if i % m == 0:
                b += i
            else:
                a += i
        return a - b