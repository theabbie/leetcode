from collections import Counter

class Solution:
    def digitCount(self, num: str) -> bool:
        n = len(num)
        ctr = Counter(num)
        for i in range(n):
            if ctr[str(i)] != int(num[i]):
                return False
        return True