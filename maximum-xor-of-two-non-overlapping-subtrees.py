class Trie:
    def __init__(self):
        self.child = {}
        
    def insert(self, number):
        cur = self
        for i in range(45, -1, -1):
            bit = (number >> i) & 1
            if bit not in cur.child:
                cur.child[bit] = Trie()
            cur = cur.child[bit]
            
    def findMax(self, number):
        cur, ans = self, 0
        for i in range(45, -1, -1):
            bit = (number >> i) & 1
            if (1-bit) in cur.child:
                cur = cur.child[1 - bit]
                ans |= (1 << i)
            elif bit in cur.child:
                cur = cur.child[bit]
            else:
                break
        return ans

class Solution:
    def maxXor(self, n: int, edges: List[List[int]], values: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        s = [0] * n
        ctr = [0] * n
        pos = [0] * n
        timer = 0
        def dfs(i, p):
            nonlocal timer
            pos[i] = timer
            timer += 1
            s[i] = values[i]
            ctr[i] = 1
            for j in graph[i]:
                if j != p:
                    dfs(j, i)
                    s[i] += s[j]
                    ctr[i] += ctr[j]
        dfs(0, -1)
        a = sorted([[pos[i], pos[i] + ctr[i] - 1, s[i]] for i in range(n)])
        b = sorted([[pos[i], pos[i] + ctr[i] - 1, s[i]] for i in range(n)], key = lambda p: p[1])
        res = 0
        trie = Trie()
        i = 0
        for x, y, v in a:
            while i < len(b) and b[i][1] < x:
                trie.insert(b[i][2])
                i += 1
            res = max(res, trie.findMax(v))
        trie = Trie()
        i = len(a) - 1
        for x, y, v in b[::-1]:
            while i >= 0 and a[i][0] > y:
                trie.insert(a[i][2])
                i -= 1
            res = max(res, trie.findMax(v))
        return res