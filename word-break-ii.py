class Solution:
    def genline(self, s, i, n, words, curr, res):
        if i >= n:
            res.append(" ".join(curr))
        for j in range(i + 1, n + 1):
            if s[i:j] in words:
                curr.append(s[i:j])
                self.genline(s, j, n, words, curr, res)
                curr.pop()
    
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        words = set(wordDict)
        res = []
        self.genline(s, 0, n, words, [], res)
        return res