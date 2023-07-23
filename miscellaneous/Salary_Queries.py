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
        
    def delete(self, s):
        curr = self.root
        curr.ctr -= 1
        for c in s:
            curr = curr.child[c]
            curr.ctr -= 1
        curr.end = True
    
    def countsmaller(self, s):
        curr = self.root
        res = 0
        n = len(s)
        for i in range(n):
            done = True
            for c in sorted(curr.child):
                if c < s[i]:
                    res += curr.child[c].ctr
                elif c == s[i]:
                    curr = curr.child[c]
                    done = False
                    break
            if done:
                break
        return res
    
n, q = map(int, input().split())

arr = list(map(int, input().split()))

padstr = lambda x: "{:010}".format(x)

trie = Trie()

for el in arr:
    trie.insert(padstr(el))

res = []

for _ in range(q):
    t, a, b = input().split()
    a, b = int(a), int(b)
    if t == "!":
        trie.delete(padstr(arr[a - 1]))
        arr[a - 1] = b
        trie.insert(padstr(arr[a - 1]))
    else:
        print(str(trie.countsmaller(padstr(b + 1)) - trie.countsmaller(padstr(a))))

print("\n".join(res))