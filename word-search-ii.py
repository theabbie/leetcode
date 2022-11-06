class Node:
  def __init__(self):
    self.child = {}
    self.end = False
    self.s = None

class Trie:
  def __init__(self):
    self.root = Node()
    
  def insert(self, s):
    curr = self.root
    for c in s:
      if c not in curr.child:
        curr.child[c] = Node()
      curr = curr.child[c]
    curr.end = True
    curr.s = s

class Solution:
    def find(self, board, i, j, m, n, node):
        if self.k == 0:
            return
        c = board[i][j]
        if c not in node.child:
            return
        node = node.child[c]
        if node.end:
            self.res.append(node.s)
            node.end = False
            node.s = None
            self.k -= 1
        board[i][j] = "#"
        for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= x < m and 0 <= y < n and board[x][y] != "#":
                self.find(board, x, y, m, n, node)
        board[i][j] = c

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        chars = set.union(*[set(r) for r in board])
        words = [w for w in words if not set(w).isdisjoint(chars)]
        self.k = len(words)
        trie = Trie()
        for w in words:
            trie.insert(w)
        self.res = []
        for i in range(m):
            for j in range(n):
                self.find(board, i, j, m, n, trie.root)
        return self.res