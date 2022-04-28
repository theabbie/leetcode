from collections import defaultdict, Counter

class Solution:
    def dfs(self, graph, node, visited):
        for j in graph[node]:
            if j not in visited:
                visited.add(j)
                self.dfs(graph, j, visited)
                
    def hammingDist(self, actr, bctr, n):
        ctr = 0
        for x in actr:
            ctr += min(actr[x], bctr[x])
        return n - ctr

    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(source)
        dist = 0
        for a, b in allowedSwaps:
            graph[a].append(b)
            graph[b].append(a)
        globalvisited = set()
        for x in graph:
            if x not in globalvisited:
                currvisited = {x}
                self.dfs(graph, x, currvisited)
                nv = len(currvisited)
                sourcenums = Counter([source[p] for p in currvisited])
                targetnums = Counter([target[p] for p in currvisited])
                dist += self.hammingDist(sourcenums, targetnums, nv)
                globalvisited.update(currvisited)
        for i in range(n):
            if i not in globalvisited and source[i] != target[i]:
                dist += 1
        return dist