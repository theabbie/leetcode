class Solution:
    def sortSentence(self, s: str) -> str:
        ogwords = s.split()
        words = ogwords[:]
        for w in ogwords:
            words[int(w[-1]) - 1] = w[:-1]
        return " ".join(words)