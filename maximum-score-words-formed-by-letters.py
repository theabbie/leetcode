class Solution:
    def maxScoreWords(self, words, letters, score):
        ctr = [0] * 26
        for c in letters:
            ctr[ord(c) - ord('a')] += 1
        @lru_cache(maxsize = None)
        def count(i, rem):
            if i >= len(words):
                return 0
            res = count(i + 1, rem)
            s = 0
            pos = True
            newrem = list(rem)
            for c in words[i]:
                if newrem[ord(c) - ord('a')] > 0:
                    s += score[ord(c) - ord('a')]
                    newrem[ord(c) - ord('a')] -= 1
                else:
                    pos = False
                    break
            if pos:
                res = max(res, s + count(i + 1, tuple(newrem)))
            return res
        return count(0, tuple(ctr))