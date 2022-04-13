class Solution:
    def sortSentence(self, s: str) -> str:
        words = sorted(s.split(), key = lambda w: int(w[-1]))
        return " ".join([w[:-1] for w in words])