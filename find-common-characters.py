from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = Counter(words[0])
        for w in words:
            res &= Counter(w)
        chars = []
        for c in res:
            chars.extend([c] * res[c])
        return chars