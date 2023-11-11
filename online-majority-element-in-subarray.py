import bisect

class TrieNode:
    def __init__(self):
        self.child = {}
        self.pos = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s, i):
        curr = self.root
        curr.pos.append(i)
        for c in s:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
            curr.pos.append(i)

    def check(self, s):
        curr = self.root
        for c in s:
            if c not in curr.child or curr.child[c].ctr == 0:
                return False
            curr = curr.child[c]
        return curr.end
    
    def majority(self, l, r, threshold):
        curr = self.root
        res = 0
        freq = 0
        while True:
            maxchild = (-1, None)
            for c in curr.child:
                ctr = bisect.bisect_right(curr.child[c].pos, r) - bisect.bisect_left(curr.child[c].pos, l)
                maxchild = max(maxchild, (ctr, c))
            if maxchild[1] != None:
                freq = maxchild[0]
                curr = curr.child[maxchild[1]]
                res = 10 * res + int(maxchild[1])
            else:
                break
        if freq < threshold:
            return -1
        return res

class MajorityChecker:
    def __init__(self, arr: List[int]):
        n = len(arr)
        self.trie = Trie()
        pad = lambda x: "{:06d}".format(x)
        for i in range(n):
            self.trie.insert(pad(arr[i]), i)

    def query(self, left: int, right: int, threshold: int) -> int:
        return self.trie.majority(left, right, threshold)