class Solution:
    def possibleStringCount(self, word):
        n = len(word)
        res = n + 1
        i = 0
        while i < n:
            while i < n - 1 and word[i] == word[i + 1]:
                i += 1
            res -= 1
            i += 1
        return res