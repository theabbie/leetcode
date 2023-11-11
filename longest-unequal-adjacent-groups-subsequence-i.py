from collections import defaultdict

class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        pos = {}
        for i in range(n):
            pos[words[i]] = i
        dp = [1] * n
        parent = {}
        for j in range(n):
            for i in range(j):
                if groups[i] != groups[j]:
                    dp[j] = max(dp[j], 1 + dp[i])
                    if dp[j] == 1 + dp[i]:
                        parent[j] = i
        res = []
        mv = max(dp)
        i = n - 1
        while dp[i] != mv:
            i -= 1
        while i in parent:
            res.append(words[i])
            i = parent[i]
        res.append(words[i])
        res.reverse()
        return res