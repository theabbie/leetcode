from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        w = []
        ctr = Counter()
        paragraph += " "
        for c in paragraph:
            if c in " !?',;.":
                if len(w) > 0:
                    ctr["".join(w)] += 1
                    w = []
            elif c.isalpha():
                w.append(c.lower())
        for w in sorted(ctr, key = lambda word: -ctr[word]):
            if w not in banned:
                return w