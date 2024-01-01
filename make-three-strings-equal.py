class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        k = 0
        while k < min(len(s1), len(s2), len(s3)) and s1[k] == s2[k] == s3[k]:
            k += 1
        if k == 0:
            return -1
        return len(s1) + len(s2) + len(s3) - 3 * k