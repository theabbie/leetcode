class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        wordset = set(words)
        res = set()
        for w in words:
            n = len(w)
            for i in range(n):
                for j in range(i + 1, n + 1):
                    if w[i:j] in wordset and (i, j) != (0, n):
                        res.add(w[i:j])
        return list(res)