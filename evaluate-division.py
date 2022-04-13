class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        n = len(equations)
        for i in range(n):
            a, b = equations[i]
            graph[a] = graph.get(a, []) + [(b, values[i])]
            graph[b] = graph.get(b, []) + [(a, 1 / values[i])]
        op = []
        for c, d in queries:
            found = False
            paths = [(c, 1, {c})]
            while len(paths) > 0:
                curr, prod, visited = paths.pop()
                if curr not in graph:
                    break
                if curr == d:
                    op.append(prod)
                    found = True
                    break
                for j, div in graph.get(curr, []):
                    if j not in visited:
                        paths.append((j, prod * div, visited.union({j})))
            if not found:
                op.append(-1.0)
        return op