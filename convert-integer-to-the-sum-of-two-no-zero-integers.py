class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1, n):
            if "0" not in str(a) and "0" not in str(n - a):
                return [a, n - a]