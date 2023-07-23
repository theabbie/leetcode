class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False
        self.ctr = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        curr = self.root
        curr.ctr += 1
        for c in s:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
            curr.ctr += 1
        curr.end = True

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        n = len(word)
        trie = Trie()
        for f in forbidden:
            trie.insert(f[::-1])
        res = 0
        currlongest = 0
        for i in range(n):
            curr = trie.root
            found = False
            x = 0
            for j in range(i, max(i - 10, -1), -1):
                if word[j] in curr.child:
                    curr = curr.child[word[j]]
                    x += 1
                    if curr.end:
                        found = True
                        break
                else:
                    break
            if found:
                currlongest = min(max(x - 1, 0), currlongest + 1)
            else:
                currlongest += 1
            res = max(res, currlongest)
        return res