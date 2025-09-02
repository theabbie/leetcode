class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Bigger:
    def __init__(self):
        self.root = TrieNode()
        self.B = 24

    def insert(self, val):
        node = self.root
        for i in range(self.B - 1, -1, -1):
            bit = (val >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
            node.count += 1

    def countBigger(self, val):
        node = self.root
        res = 0
        for i in range(self.B - 1, -1, -1):
            bit = (val >> i) & 1
            if bit == 0 and 1 in node.children:
                res += node.children[1].count
            if bit not in node.children:
                break
            node = node.children[bit]
        return res
    
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10 ** 9 + 7
        ctr = Counter()
        bg = Bigger()
        res = 0
        x = 0
        for el in instructions:
            v = bg.countBigger(el)
            res += min(v, x - ctr[el] - v)
            res %= MOD
            bg.insert(el)
            ctr[el] += 1
            x += 1
        return res