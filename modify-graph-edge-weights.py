class Solution:
    def modifiedGraphEdges(self, n, edges, source, destination, target):
        INF = 2 * 10 ** 9
        def calculate():
            graph = [[] for _ in range(n)]
            for u, v, w in edges:
                graph[u].append((v, w))
                graph[v].append((u, w))
            heap = [(0, source)]
            dist = [float('inf')] * n
            dist[source] = 0
            while heap:
                d, i = heapq.heappop(heap)
                if i == destination:
                    return d
                for j, w in graph[i]:
                    if dist[j] > d + w:
                        dist[j] = d + w
                        heapq.heappush(heap, (dist[j], j))
            return float('inf')
        mod = set()
        for i in range(len(edges)):
            if edges[i][2] == -1:
                mod.add(i)
        for i in mod:
            edges[i][2] = INF
        curr = calculate()
        if curr == target:
            return edges
        if curr < target:
            return []
        for i in mod:
            edges[i][2] = 1
        if calculate() > target:
            return []
        for i in mod:
            edges[i][2] = INF
        for i in mod:
            edges[i][2] = 1
            curr = calculate()
            if curr <= target:
                edges[i][2] += target - curr
                return edges
        return []