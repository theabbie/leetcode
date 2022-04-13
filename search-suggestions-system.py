class Node:
    def __init__(self, val=None, children=[], end=False):
        self.val = val
        self.children = children
        self.end = end
        self.words = set()

class Trie:
    def __init__(self):
        self.root = Node(val=None, children=[])

    def insert(self, word: str, pos) -> None:
        n = len(word)
        curr = self.root
        for i, c in enumerate(word):
            found = False
            for node in curr.children:
                if node.val == c:
                    curr = node
                    curr.words.add(pos)
                    found = True
                    break
            if not found:
                newcurr = Node(val=c, children=[])
                newcurr.words.add(pos)
                curr.children.append(newcurr)
                curr = newcurr
        curr.end = True

    def startsWith(self, prefix: str):
        n = len(prefix)
        curr = self.root
        for i, c in enumerate(prefix):
            found = False
            for node in curr.children:
                if node.val == c:
                    curr = node
                    found = True
                    break
            if not found:
                return []
        return curr.words

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for i, p in enumerate(products):
            trie.insert(p, i)
        n = len(searchWord)
        op = []
        for i in range(1, n + 1):
            res = trie.startsWith(searchWord[:i])
            op.append(sorted([products[i] for i in res])[:3])
        return op