class Solution:
    def genline(self, s, i, n, words, curr, res):
        if i >= n:
            res.append(curr[:])
        for j in range(i + 1, n + 1):
            if s[i:j] in words:
                curr.append(s[i:j])
                self.genline(s, j, n, words, curr, res)
                curr.pop()
    
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordset = set(words)
        res = []
        for w in words:
            curr = []
            found = False
            self.genline(w, 0, len(w), wordset, [], curr)
            for l in curr:
                if len(l) > 1:
                    found = True
                    break
            if found:
                res.append(w)
        return res