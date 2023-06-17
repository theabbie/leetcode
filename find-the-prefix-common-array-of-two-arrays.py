from collections import Counter

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        res = [0] * n
        a = Counter()
        b = Counter()
        for i in range(n):
            a[A[i]] += 1
            b[B[i]] += 1
            for el in a:
                if el in b:
                    res[i] += min(a[el], b[el])
        return res