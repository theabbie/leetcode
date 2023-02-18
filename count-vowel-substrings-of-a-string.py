from collections import Counter

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        res = 0
        def valid(c):
            return len(c) == 5 and ctr['a'] > 0 and ctr['e'] > 0 and ctr['i'] > 0 and ctr['o'] > 0 and ctr['u'] > 0
        for i in range(n):
            ctr = Counter()
            for j in range(i, n):
                ctr[word[j]] += 1
                if valid(ctr):
                    res += 1
        return res