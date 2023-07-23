import random

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

s = list("0123456789" * 10)

random.shuffle(s)

s = "".join(s)

s = ""

for i in range(100):
    s += "{:03}".format(i)

print("Input:", s)

n = len(s)

trie = Trie()

for i in range(n):
    trie.insert(s[i:])
    
def count(num, i, n, tight, zero, root, cache):
    if i >= n:
        return 1
    key = (i, tight, zero, root)
    if key in cache:
        return cache[key]
    maxd = 9
    if tight:
        maxd = int(num[i])
    res = 0
    for d in range(maxd + 1):
        currzero = zero and d == 0
        newroot = root
        if not currzero:
            if str(d) not in root.child:
                continue
            newroot = root.child[str(d)]
        res += count(num, i + 1, n, tight and d == maxd, currzero, newroot, cache)
    cache[key] = res
    return res

end = 1
while count(str(end), 0, len(str(end)), True, True, trie.root, {}) == end + 1:
    end *= 2

beg = end // 2
res = -1

while beg <= end:
    mid = (beg + end) // 2
    if count(str(mid), 0, len(str(mid)), True, True, trie.root, {}) == mid + 1:
        beg = mid + 1
    else:
        res = mid
        end = mid - 1

print("Output:", res)