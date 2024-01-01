class Solution:
    def check(self, s1, s2):
        n = len(s1)
        ctr = [0] * 26
        for c in s2:
            ctr[ord(c) - ord('a')] += 1
        for c in s1:
            x = ord(c) - ord('a')
            done = False
            for d in range(x, 26):
                if ctr[d] > 0:
                    ctr[d] -= 1
                    done = True
                    break
            if not done:
                return False
        return True
    
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        return self.check(s1, s2) or self.check(s2, s1)