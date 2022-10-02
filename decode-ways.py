class Solution:
    def isCorrect(self, n):
        if n[0] == "0":
            return False
        return int(n) >= 1 and int(n) <= 26
    
    def numDecodingsRec(self, s):
        if len(s) == 0:
            return 1
        if len(s) == 1:
            if self.isCorrect(s):
                return 1
            else:
                return 0
        if s in self.memo:
            return self.memo[s]
        numWays = 0
        if self.isCorrect(s[:1]):
            numWays += self.numDecodingsRec(s[1:])
        if self.isCorrect(s[:2]):
            numWays += self.numDecodingsRec(s[2:])
        self.memo[s] = numWays
        return numWays
    
    def numDecodings(self, s: str) -> int:
        self.memo = {}
        return self.numDecodingsRec(s)