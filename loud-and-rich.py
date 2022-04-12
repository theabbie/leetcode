class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = {}
        for a, b in richer:
            graph[b] = graph.get(b, []) + [a]
        answer = [0] * n
        for beg in range(n):
            paths = [beg]
            visited = {beg}
            while len(paths) > 0:
                curr = paths.pop()
                for j in graph.get(curr, []):
                    if j not in visited:
                        visited.add(j)
                        paths.append(j)
            answer[beg] = min(visited, key = lambda p: quiet[p])
        return answer