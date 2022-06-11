from collections import defaultdict
import re

class Solution:
    def DFS(self, graph, node, v):
        v.add(node)
        for j in graph[node]:
            if j not in v:
                self.DFS(graph, j, v)
    
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        reachable = defaultdict(set)
        for a, b in mappings:
            reachable[a].add(b)
        for c in sub:
            reachable[c].add(c)
        regex = ""
        for c in sub:
            if len(reachable[c]) > 1:
                regex += "("
                regex += "|".join(reachable[c])
                regex += ")"
            else:
                regex += c
        return re.compile(regex).search(s)