class Solution:
    def isLeave(self, s1, s2, s3, i, j, k, m, n, p):
        if (i, j, k) in self.cache:
            return self.cache[(i,j,k)]
        if i >= m or j >= n or k >= p:
            if i >= m:
                res = s2[j:] == s3[k:]
                self.cache[(i,j,k)] = res
                return res
            if j >= n:
                res = s1[i:] == s3[k:]
                self.cache[(i,j,k)] = res
                return res
            self.cache[(i,j,k)] = False
            return False
        if s1[i] == s3[k] and self.isLeave(s1, s2, s3, i + 1, j, k + 1, m, n, p):
            self.cache[(i,j,k)] = True
            return True
        if s2[j] == s3[k] and self.isLeave(s1, s2, s3, i, j + 1, k + 1, m, n, p):
            self.cache[(i,j,k)] = True
            return True
        self.cache[(i,j,k)] = False
        return False
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        p = len(s3)
        self.cache = {}
        return self.isLeave(s1, s2, s3, 0, 0, 0, m, n, p)