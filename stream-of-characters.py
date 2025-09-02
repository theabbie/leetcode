class Node(defaultdict):
    def __init__(self):
        super().__init__(Node)
        self.end = False

class StreamChecker:
    def __init__(self, words: List[str]):
        self.k = max(len(w) for w in words)
        self.trie = Node()
        for w in words:
            curr = self.trie
            for c in w[::-1]:
                curr = curr[c]
            curr.end = True
        self.q = deque()

    def query(self, letter: str) -> bool:
        self.q.appendleft(letter)
        if len(self.q) > self.k:
            self.q.pop()
        curr = self.trie
        for c in self.q:
            if c not in curr:
                return False
            curr = curr[c]
            if curr.end:
                return True
        return False