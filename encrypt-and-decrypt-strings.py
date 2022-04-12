class Node:
    def __init__(self, val=None, children={}, end=False):
        self.val = val
        self.children = children
        self.end = end

class Trie:
    def __init__(self):
        self.root = Node(val=None, children={})

    def insert(self, word: str) -> None:
        n = len(word)
        curr = self.root
        for i, c in enumerate(word):
            if c in curr.children:
                curr = curr.children[c]
            else:
                newcurr = Node(val=c, children={})
                curr.children[c] = newcurr
                curr = newcurr
        curr.end = True

class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.trie = Trie()
        for word in dictionary:
            self.trie.insert(word)
        self.encmap = {}
        self.decmap = {}
        n = len(keys)
        for i in range(n):
            self.encmap[keys[i]] = values[i]
            self.decmap[values[i]] = self.decmap.get(values[i], []) + [keys[i]]

    def encrypt(self, word1: str) -> str:
        return "".join([self.encmap[c] for c in word1])

    def decrypt(self, word2: str) -> int:
        n = len(word2)
        ctr = 0
        chunks = [word2[i:i+2] for i in range(0, n, 2)]
        stack = [(self.trie.root, "", 0)]
        while len(stack) > 0:
            curr, currstr, i = stack.pop()
            if i == len(chunks) and curr.end:
                ctr += 1
            if i < len(chunks):
                for nchunk in self.decmap.get(chunks[i], []):
                    if nchunk in curr.children:
                        stack.append((curr.children[nchunk], currstr + nchunk, i + 1))
        return ctr

# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)