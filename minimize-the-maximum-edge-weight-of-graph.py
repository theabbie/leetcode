class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        def check(up):
            graph = [[] for _ in range(n)]
            v = [False] * n
            for a, b, w in edges:
                if w <= up:
                    graph[b].append(a)
            stack = [0]
            v[0] = True
            while stack:
                i = stack.pop()
                for j in graph[i]:
                    if not v[j]:
                        v[j] = True
                        stack.append(j)
            return not (False in v)
        ws = set()
        for a, b, w in edges:
            ws.add(w)
        ws = sorted(ws)
        beg = 0
        end = len(ws) - 1
        while beg <= end:
            mid = (beg + end) // 2
            up = ws[mid]
            if check(up):
                end = mid - 1
            else:
                beg = mid + 1
        return ws[end + 1] if end + 1 < len(ws) else -1