class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0
        req = (1 << n) - 1
        visited = {}
        queue = []
        for i in range(n):
            queue.append((0 | (1 << i), i))
        lvl = 1
        while len(queue) > 0:
            k = len(queue)
            while k > 0:
                curr, currnode = queue.pop(0)
                for u in graph[currnode]:
                    newMask = curr | (1 << u)
                    if newMask == req:
                        return lvl
                    if newMask in visited.get(u, {}):
                        continue
                    visited[u] = visited.get(u, set()).union({newMask})
                    queue.append((newMask, u))
                k -= 1
            lvl += 1
        return -1