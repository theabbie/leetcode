class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        root = TrieNode()
        for w in wordDict:
            curr = root
            for c in w:
                if c not in curr.child:
                    curr.child[c] = TrieNode()
                curr = curr.child[c]
            curr.end = True
        dp = [False] * (n + 1)
        dp[n] = True
        for i in range(n - 1, -1, -1):
            j = i
            curr = root
            while j < n and curr:
                curr = curr.child.get(s[j], None)
                if curr and curr.end and dp[j + 1]:
                    dp[i] = True
                    break
                j += 1
        return dp[0]