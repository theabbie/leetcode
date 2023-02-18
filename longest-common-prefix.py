class Node:
    def __init__(self):
        self.child = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = Node()
        self.minl = float('inf')

    def insert(self, s):
        self.minl = min(self.minl, len(s))
        curr = self.root
        for c in s:
            if c not in curr.child:
                curr.child[c] = Node()
            curr = curr.child[c]
        curr.end = True
        
    def longestprefix(self):
        res = []
        curr = self.root
        while curr and len(curr.child) == 1 and len(res) < self.minl:
            c = min(curr.child)
            res.append(c)
            curr = curr.child[c]
        return "".join(res)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        minl = float('inf')
        for s in strs:
            trie.insert(s)
        return trie.longestprefix()