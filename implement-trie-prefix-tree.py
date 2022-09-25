class Node:
    def __init__(self):
        self.child = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()
        
    def check(self, s):
        curr = self.root
        for c in s:
            if c not in curr.child:
                return None
            curr = curr.child[c]
        return curr

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = Node()
            curr = curr.child[c]
        curr.end = True

    def search(self, word: str) -> bool:
        res = self.check(word)
        return res and res.end

    def startsWith(self, prefix: str) -> bool:
        res = self.check(prefix)
        return bool(res)