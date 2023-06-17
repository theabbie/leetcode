class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False
        self.ctr = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        curr = self.root
        curr.ctr += 1
        for c in s:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
            curr.ctr += 1
        curr.end = True
    
    def kthsmallest(self, k):
        curr = self.root
        res = 0
        while True:
            done = True
            for c in sorted(curr.child):
                if k > curr.child[c].ctr:
                    k -= curr.child[c].ctr
                else:
                    res = 10 * res + int(c)
                    curr = curr.child[c]
                    done = False
                    break
            if done:
                break
        return res

class MedianFinder:
    def __init__(self):
        self.trie = Trie()

    def addNum(self, num: int) -> None:
        self.trie.insert("{:06}".format(100000 + num))

    def findMedian(self) -> float:
        k = self.trie.root.ctr
        kmeans = [(k - 1) // 2, k // 2]
        s = 0
        for pos in kmeans:
            s += self.trie.kthsmallest(pos + 1) - 100000
        return s / 2