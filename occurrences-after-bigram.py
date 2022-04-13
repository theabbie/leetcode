class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        n = len(words)
        fpos = set()
        spos = set()
        for i, word in enumerate(words):
            if word == first:
                fpos.add(i)
            if word == second:
                spos.add(i)
        third = []
        for i in range(n):
            if (i - 1) in spos and (i - 2) in fpos:
                third.append(words[i])
        return third