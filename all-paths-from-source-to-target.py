class Solution:
    def getPath(self, beg, end, graph, v, path):
        if beg == end:
            self.paths.append(path[:])
        for node in graph[beg]:
            if node not in v:
                path.append(node)
                v.add(node)
                self.getPath(node, end, graph, v, path)
                path.pop()
                v.remove(node)
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        self.paths = []
        self.getPath(0, n - 1, graph, {0}, [0])
        return self.paths