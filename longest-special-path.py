class Stack:
    def __init__(self):
        self.s = [(-1, 0)]
        self.pos = defaultdict(lambda: [-1])
    
    def push(self, x):
        l = min(1 + self.s[-1][1], len(self.s) - self.pos[x][-1])
        self.s.append((x, l))
        self.pos[x].append(len(self.s) - 1)
        
    def pop(self):
        self.pos[self.s.pop()[0]].pop()
        
    def getl(self):
        return self.s[-1][1]

class Solution:
    def longestSpecialPath(self, edges, nums):
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v, l in edges:
            graph[u].append((v, l))
            graph[v].append((u, l))
        res = (float('inf'), float('inf'))
        stack = Stack()
        psum = [0]
        def dfs(i, prev):
            nonlocal res
            stack.push(nums[i])
            l = stack.getl()
            s = psum[-1] - psum[-1-l+1]
            res = min(res, (-s, l))
            for j, l in graph[i]:
                if j == prev:
                    continue
                psum.append(psum[-1] + l)
                dfs(j, i)
                psum.pop()
            stack.pop()
        dfs(0, -1)
        return [-res[0], res[1]]