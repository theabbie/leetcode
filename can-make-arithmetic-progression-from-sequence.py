from collections import Counter

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        if n == 1:
            return True
        arr = Counter(arr)
        a = min(arr)
        b = max(arr)
        d = (b - a) // (n - 1)
        if d == 0 and len(arr) == 1:
            return True
        for i in range(n):
            if arr[a + i * d] != 1:
                return False
        return True