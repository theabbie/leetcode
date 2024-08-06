class TrieNode:
    def __init__(self):
        self.child = {}
        self.min = (float('inf'), float('inf'))

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s, i):
        curr = self.root
        curr.min = min(curr.min, (len(s), i))
        for c in s:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
            curr.min = min(curr.min, (len(s), i))
            
    def get(self, s):
        curr = self.root
        l = 0
        for c in s:
            if c not in curr.child:
                break
            l += 1
            curr = curr.child[c]
        curr = self.root
        for c in s[:l]:
            curr = curr.child[c]
        return curr.min[1]

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = Trie()
        for i, w in enumerate(wordsContainer):
            trie.insert(w[::-1], i)
        res = []
        for w in wordsQuery:
            res.append(trie.get(w[::-1]))
        return res