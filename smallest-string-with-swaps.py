from collections import defaultdict

class Solution:
    def dfs(self, graph, node, visited):
        for j in graph[node]:
            if j not in visited:
                visited.add(j)
                self.dfs(graph, j, visited)
    
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        op = list(s)
        graph = defaultdict(list)
        for a, b in pairs:
            graph[a].append(b)
            graph[b].append(a)
        globalvisited = set()
        for x in graph:
            if x not in globalvisited:
                currvisited = {x}
                self.dfs(graph, x, currvisited)
                indexes = sorted(currvisited)
                indexes_asc = sorted(currvisited, key = lambda p: s[p])
                n = len(indexes)
                for i in range(n):
                    op[indexes[i]] = s[indexes_asc[i]]
                globalvisited.update(currvisited)
        return "".join(op)