class Solution:
    def strech(self, s, i, j, n):
        l = 0
        while i - l >= 0 and j + l < n and s[i - l] == s[j + l]:
            self.pals.add((i - l, j + l + 1))
            l += 1
    
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        self.pals = set()
        for i in range(n):
            for a, b in [(i, i), (i, i + 1)]:
                self.strech(s, a, b, n)
        for i in range(1, n):
            for j in range(i, n):
                if (0, i) in self.pals and (i, j) in self.pals and (j, n) in self.pals:
                    return True
        return False