def compute_lps(pattern):
    length = 0
    lps = [0] * len(pattern)
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def find_pattern_indices(string, pattern):
    indices = []
    n = len(string)
    m = len(pattern)
    lps = compute_lps(pattern)
    i = j = 0
    while i < n:
        if string[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                indices.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return indices

class TrieNode:
    def __init__(self):
        self.child = {}
        self.cost = float('inf')
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
 
    def insert(self, s, cost):
        curr = self.root
        for c in s:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.cost = min(curr.cost, cost)

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        n = len(target)
        dp = [float('inf')] * (n + 1)
        dp[n] = 0
        vals = [(words[i], costs[i]) for i in range(len(words))]
        vals.sort(key = lambda x: -len(x[0]))
        K = sum(len(w) for w in words)
        mincosts = [[] for _ in range(n)]
        trie = Trie()
        for w, c in vals:
            l = len(w)
            if l * l <= K:
                trie.insert(w, c)
                continue
            for i in find_pattern_indices(target, w):
                mincosts[i].append((l, c))
        for i in range(n - 1, -1, -1):
            j = i
            root = trie.root
            while j < n and target[j] in root.child:
                root = root.child[target[j]]
                dp[i] = min(dp[i], root.cost + dp[j + 1])
                l = j - i + 1
                if l * l > K:
                    break
                j += 1
            for l, c in mincosts[i]:
                dp[i] = min(dp[i], c + dp[i + l])
        return dp[0] if dp[0] != float('inf') else -1