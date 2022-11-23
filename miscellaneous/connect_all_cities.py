t = int(input())

class Node:
  def __init__(self):
    self.child = {}
    self.end = False


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

  def valid(self, s, i, n, root):
    if i >= n:
        return False
    if s[i] == "0":
        res = True
        if "0" in root.child:
            res = res and self.valid(s, i + 1, n, root.child["0"])
        if "1" in root.child:
            res = res and self.valid(s, i + 1, n, root.child["1"])
        return res
    elif "0" in root.child:
        return self.valid(s, i + 1, n, root.child["0"])
    else:
        return True

  def minimum(self, s, i, n, val, root):
    if i >= n:
        if val > 0:
            return val
        return float('inf')
    res = float('inf')
    if "0" in root.child:
        res = min(res, self.minimum(s, i + 1, n, 2 * val, root.child["0"]))
    if "1" in root.child:
        res = min(res, self.minimum(s, i + 1, n, 2 * val + int(s[i]), root.child["1"]))
    return res

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    trie = Trie()
    ctr = [0] * 32
    for el in arr:
        trie.insert("{:032b}".format(el))
        for b in range(32):
            if el & (1 << b):
                ctr[b] += 1
    res = 0
    for el in arr:
        res += trie.minimum("{:032b}".format(el), 0, 32, 0, trie.root)
    print(res)
