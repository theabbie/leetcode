import bisect

class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False
        self.pos = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s, pos):
        curr = self.root
        curr.pos.append(pos)
        for c in s:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
            curr.pos.append(pos)
        curr.end = True
    
    def kthsmallest(self, k, l, r):
        curr = self.root
        res = 0
        while True:
            done = True
            for c in sorted(curr.child):
                ctr = bisect.bisect_right(curr.child[c].pos, r) - bisect.bisect_left(curr.child[c].pos, l)
                if k > ctr:
                    k -= ctr
                else:
                    res = 10 * res + int(c)
                    curr = curr.child[c]
                    done = False
                    break
            if done:
                break
        return res
    
trie = Trie()
padstr = lambda x: "{:011}".format(1000000000 + x)

n, q = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(n):
    trie.insert(padstr(arr[i]), i)

for _ in range(q):
    l, r, k = map(int, input().split())
    print(trie.kthsmallest(k, l - 1, r - 1) - 1000000000)