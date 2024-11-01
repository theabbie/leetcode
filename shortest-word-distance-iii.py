class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        res = float('inf')
        a = [i for i in range(len(wordsDict)) if wordsDict[i] == word1]
        b = [i for i in range(len(wordsDict)) if wordsDict[i] == word2]
        if len(a) > len(b):
            a, b = b, a
        if word1 == word2:
            return min(a[i + 1] - a[i] for i in range(len(a) - 1))
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