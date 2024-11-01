from collections import defaultdict

class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.pos = defaultdict(list)
        for i in range(len(wordsDict)):
            self.pos[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        res = float('inf')
        a = self.pos[word1]
        b = self.pos[word2]
        if len(a) > len(b):
            a, b = b, a
        i = 0
        for j in range(len(a)):
            while i < len(b) and b[i] <= a[j]:
                res = min(res, a[j] - b[i])
                i += 1
        i = len(b) - 1
        for j in range(len(a) - 1, -1, -1):
            while i >= 0 and b[i] >= a[j]:
                res = min(res, b[i] - a[j])
                i -= 1
        return res