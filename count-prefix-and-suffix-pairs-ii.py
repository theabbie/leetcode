def Z(s):
    n = len(s)
    Z = [0] * n
    l = r = 0
    for i in range(1, n):
        z = Z[i - l]
        if i + z >= r:
            z = max(r - i, 0)
            while i + z < n and s[z] == s[i + z]:
                z += 1
            l, r = i, i + z
        Z[i] = z
    Z[0] = n
    return Z

class TrieNode:
    def __init__(self):
        self.child = {}
        self.ctr = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        n = len(s)
        curr = self.root
        for c in s:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.ctr += 1

    def check(self, s):
        curr = self.root
        z = Z(s)
        res = 0
        l = 0
        for c in s:
            if c not in curr.child:
                return res
            curr = curr.child[c]
            l += 1
            if z[-l] == l:
                res += curr.ctr
        return res

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        pref = Trie()
        res = 0
        for i in range(n):
            res += pref.check(words[i])
            pref.insert(words[i])
        return res