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
        curr.ctr += 1
        l = 0
        for c in s:
            l += 1
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
            if s[:l] == s[-l:]:
                curr.ctr += 1

    def check(self, s):
        curr = self.root
        for c in s:
            if c not in curr.child:
                return 0
            curr = curr.child[c]
        return curr.ctr

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        pref = Trie()
        res = 0
        for j in range(n - 1, -1, -1):
            res += pref.check(words[j])
            pref.insert(words[j])
        return res