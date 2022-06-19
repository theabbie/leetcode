class Node:
    def __init__(self, val, children, words):
        self.val = val
        self.children = children
        self.words = words

class Trie:
    def __init__(self):
        self.root = Node(None, {}, set())

    def insert(self, word, pos) -> None:
        n = len(word)
        curr = self.root
        for i, c in enumerate(word):
            if c in curr.children:
                curr = curr.children[c]
            else:
                newcurr = Node(c, {}, set())
                curr.children[c] = newcurr
                curr = newcurr
            curr.words.add(pos)
        
    def startsWith(self, prefix, res):
        n = len(prefix)
        curr = self.root
        for i, c in enumerate(prefix):
            if c in curr.children:
                curr = curr.children[c]
                res.append(curr.words)
            else:
                return set()
        return curr.words

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        n = len(searchWord)
        trie = Trie()
        for i, product in enumerate(products):
            trie.insert(product, i)
        res = []
        trie.startsWith(searchWord, res)
        while len(res) < n:
            res.append({})
        return [sorted([products[i] for i in curr])[:3] for curr in res]