class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m != n:
            return False
        if s1 == s2:
            return True
        s1diff = []
        s2diff = []
        for i in range(n):
            if s1[i] != s2[i]:
                s1diff.append(s1[i])
                s2diff.append(s2[i])
        if not len(s1diff) == len(s2diff) == 2:
            return False
        return sorted(s1diff) == sorted(s2diff)