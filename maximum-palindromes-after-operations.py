from collections import Counter

class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        n = len(words)
        words.sort(key = lambda x: len(x))
        ctr = Counter()
        for w in words:
            ctr += Counter(w)
        evens = []
        for w in words:
            evens.append(2 * (len(w) // 2))
        evens.sort()
        for c in sorted(ctr, key = lambda x: ctr[x]):
            for i in range(len(evens)):
                give = min(2 * (ctr[c] // 2), evens[i])
                evens[i] -= give
                ctr[c] -= give
        return evens.count(0)