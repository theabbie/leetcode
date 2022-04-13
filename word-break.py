class Solution:
    memo = {}
    
    def wordBreakRec(self, s, beg, end, wordSet):
        if (beg, end) in self.memo:
            return self.memo[(beg, end)]
        n = len(s)
        if s[beg:end] in wordSet:
            self.memo[(beg, end)] = True
            return self.memo[(beg, end)]
        for i in range(beg, end):
            if self.wordBreakRec(s, beg, i, wordSet) and self.wordBreakRec(s, i, end, wordSet):
                self.memo[(beg, end)] = True
                return self.memo[(beg, end)]
        self.memo[(beg, end)] = False
        return self.memo[(beg, end)]

    def wordBreak(self, s: str, wordDict):
        self.memo = {}
        n = len(s)
        wordSet = set()
        for word in wordDict:
            wordSet.add(word)
        return self.wordBreakRec(s, 0, n, wordSet)