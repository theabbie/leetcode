class Node:
    def __init__(self, val, children, words, type):
        self.val = val
        self.children = children
        self.words = words
        self.type = type

class Trie:
    def __init__(self):
        self.root = Node(None, {}, set(), 0)

    def insert(self, word: str, pos, type) -> None:
        n = len(word)
        curr = self.root
        for i, c in enumerate(word):
            if (c, type) in curr.children:
                curr = curr.children[(c, type)]
            else:
                newcurr = Node(val=c, children={}, words=set(), type=type)
                curr.children[(c, type)] = newcurr
                curr = newcurr
            curr.words.add(pos)
        
    def startsWith(self, prefix: str, type):
        n = len(prefix)
        curr = self.root
        for i, c in enumerate(prefix):
            if (c, type) in curr.children:
                curr = curr.children[(c, type)]
            else:
                return set()
        return curr.words

class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.trie = Trie()
        n = len(words)
        for i in range(n):
            self.trie.insert(words[i], i, 1)
            self.trie.insert(words[i][::-1], i, -1)
        self.cache = {}

    def f(self, prefix: str, suffix: str) -> int:
        key = (prefix, suffix)
        if key in self.cache:
            return self.cache[key]
        beg = self.trie.startsWith(prefix, 1)
        end = self.trie.startsWith(suffix[::-1], -1)
        res = set.intersection(beg, end)
        if len(res) == 0:
            self.cache[key] = -1
            return -1
        res = max(res)
        self.cache[key] = res
        return res

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)