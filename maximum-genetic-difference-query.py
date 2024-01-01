class Node:
    def __init__(self):
        self.child = [None, None]
        self.ctr = 0

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, s):
        curr = self.root
        curr.ctr += 1
        for c in s:
            c = int(c)
            if curr.child[c] == None:
                curr.child[c] = Node()
            curr = curr.child[c]
            curr.ctr += 1
            
    def delete(self, s):
        curr = self.root
        curr.ctr -= 1
        for c in s:
            c = int(c)
            if curr.child[c].ctr == 1:
                curr.child[c] = None
                break
            curr = curr.child[c]
            curr.ctr -= 1
        
    def getmax(self, s):
        curr = self.root
        res = 0
        for c in s:
            c = int(c)
            if curr.child[1 - c] != None and curr.child[1 - c].ctr > 0:
                curr = curr.child[1 - c]
                res = 2 * res + 1
            elif curr.child[c] != None and curr.child[c].ctr > 0:
                curr = curr.child[c]
                res = 2 * res
        return res

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        n = len(parents)
        q = [[] for _ in range(n)]
        res = [0] * len(queries)
        for i in range(len(queries)):
            q[queries[i][0]].append((queries[i][1], i))
        graph = [[] for _ in range(n)]
        root = 0
        for i in range(n):
            if parents[i] == -1:
                root = i
                continue
            graph[parents[i]].append(i)
        val = lambda x: "{:018b}".format(x)
        trie = Trie()
        def dfs(curr):
            trie.insert(val(curr))
            for x, pos in q[curr]:
                res[pos] = trie.getmax(val(x))
            for j in graph[curr]:
                dfs(j)
            trie.delete(val(curr))
        dfs(root)
        return res