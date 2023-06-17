class Node:
    def __init__(self, val=None, children=[], end=False):
        self.val = val
        self.children = children
        self.end = end

class WordDictionary:

    def __init__(self):
        self.root = Node(val=None, children=[])

    def addWord(self, word: str) -> None:
        n = len(word)
        curr = self.root
        for i, c in enumerate(word):
            found = False
            for node in curr.children:
                if node.val == c:
                    curr = node
                    found = True
                    break
            if not found:
                newcurr = Node(val=c, children=[])
                curr.children.append(newcurr)
                curr = newcurr
        curr.end = True

    def search(self, word: str) -> bool:
        n = len(word)
        paths = [(self.root, 0)]
        while len(paths) > 0:
            curr, i = paths.pop()
            if i == n and curr.end:
                return True
            if curr.children and i < n:
                for c in curr.children:
                    if word[i] == "." or c.val == word[i]:
                        paths.append((c, i + 1))
        return False