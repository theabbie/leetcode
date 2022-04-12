class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        types = [1] * n
        graph = {}
        for a, b in paths:
            graph[a - 1] = graph.get(a - 1, []) + [b - 1]
            graph[b - 1] = graph.get(b - 1, []) + [a - 1]
        visited = set()
        stack = list(range(n))
        while len(stack) > 0:
            curr = stack.pop()
            visited.add(curr)
            colors = set()
            for j in graph.get(curr, []):
                colors.add(types[j])
                if j not in visited:
                    stack.append(j)
            if types[curr] in colors:
                for i in range(1, n + 1):
                    if i not in colors:
                        types[curr] = i
                        break
        return types