class Solution:
    memo = {}
    
    def wordBreakRec(self, s, beg, end, wordSet):
        key = 5000 * beg + end
        if key in self.memo:
            return self.memo[key]
        n = len(s)
        if s[beg:end] in wordSet:
            self.memo[key] = True
            return True
        for i in range(beg, end):
            if self.wordBreakRec(s, beg, i, wordSet) and self.wordBreakRec(s, i, end, wordSet):
                self.memo[key] = True
                return True
        self.memo[key] = False
        return False

    def wordBreak(self, s: str, wordDict):
        self.memo = {}
        n = len(s)
        wordSet = set()
        for word in wordDict:
            wordSet.add(word)
        return self.wordBreakRec(s, 0, n, wordSet)