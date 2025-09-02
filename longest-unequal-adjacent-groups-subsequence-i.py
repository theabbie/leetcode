class Solution:
    def getLongestSubsequence(self, words, groups):
        n = len(words)
        prev = -1
        res = []
        for i in range(n):
            if prev == -1 or groups[i] != groups[prev]:
                res.append(words[i])
                prev = i
        return res