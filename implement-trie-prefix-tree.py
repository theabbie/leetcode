class Node:
    def __init__(self, val=None, children=[], end=False):
        self.val = val
        self.children = children
        self.end = end

class Trie:
    def __init__(self):
        self.root = Node(val=None, children=[])

    def insert(self, word: str) -> None:
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
        curr = self.root
        for i, c in enumerate(word):
            found = False
            for node in curr.children:
                if node.val == c:
                    curr = node
                    found = True
                    break
            if not found:
                return False
        return curr.end

    def startsWith(self, prefix: str) -> bool:
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
                return False
        return True

# class Trie:

#     def __init__(self):
#         self.trie = {}

#     def insert(self, word: str) -> None:
#         word = list(word) + [-1]
#         n = len(word)
#         for i in range(n - 1):
#             if i not in self.trie:
#                 self.trie[i] = {}
#             if word[i] in self.trie[i]:
#                 self.trie[i][word[i]].add(word[i + 1])
#             else:
#                 self.trie[i][word[i]] = {word[i + 1]}

#     def search(self, word: str, isPartial = False) -> bool:
#         if not isPartial:
#             word = list(word) + [-1]
#         n = len(word)
#         if n == 1:
#             if word[0] in self.trie.get(0, {}):
#                 return True
#             else:
#                 return False
#         for i in range(n - 1):
#             if i not in self.trie or word[i] not in self.trie[i] or word[i + 1] not in self.trie[i][word[i]]:
#                 return False
#         return True

#     def startsWith(self, prefix: str) -> bool:
#         return self.search(prefix, isPartial = True)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)