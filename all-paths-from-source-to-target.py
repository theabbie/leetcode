class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        op = []
        paths = [([0], {0})]
        while len(paths) > 0:
            curr, visited = paths.pop()
            if curr[-1] == n - 1:
                op.append(curr)
            for newcurr in graph[curr[-1]]:
                if newcurr not in visited:
                    paths.append((curr + [newcurr], visited.union({newcurr})))
        return op