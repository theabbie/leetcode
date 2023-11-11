from collections import defaultdict

class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        pos = {}
        for i in range(n):
            pos[words[i]] = i
        dp = [1] * n
        parent = {}
        for i in range(n):
            s = words[i]
            m = len(s)
            for j in range(m):
                for k in range(26):
                    c = chr(ord('a') + k)
                    if c == s[j]:
                        continue
                    ss = s[:j] + c + s[j+1:]
                    if ss in pos and pos[ss] < i and groups[pos[ss]] != groups[i]:
                        dp[i] = max(dp[i], 1 + dp[pos[ss]])
                        if dp[i] == 1 + dp[pos[ss]]:
                            parent[i] = pos[ss]
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