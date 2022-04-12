class Solution:
    memo = {}
    
    def wordBreakRec(self, s, beg, end, wordSet):
        if (beg, end) in self.memo:
            return self.memo[(beg, end)]
        n = len(s)
        if s[beg:end] in wordSet:
            self.memo[(beg, end)] = True
            return True
        isGood = False
        for i in range(beg, end):
            if self.wordBreakRec(s, beg, i, wordSet) and self.wordBreakRec(s, i, end, wordSet):
                isGood = True
        return isGood

    def wordBreak(self, s: str, wordDict):
        self.memo = {}
        n = len(s)
        wordSet = set()
        for word in wordDict:
            wordSet.add(word)
        self.wordBreakRec(s, 0, n, wordSet)
        print(list(self.memo.keys()))

Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])