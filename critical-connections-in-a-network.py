class Solution:
    def criticalConnections(self, n, connections):
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        timer = 0
        cin = [-1] * n
        res = []
        def find(i, prev):
            nonlocal timer
            cin[i] = timer
            timer += 1
            mincin = float('inf')
            for j in graph[i]:
                if cin[j] == -1:
                    currmincin = find(j, i)
                    mincin = min(mincin, currmincin)
                    if currmincin > cin[i]:
                        res.append((i, j))
                elif j != prev:
                    mincin = min(mincin, cin[j])
            return mincin
        find(0, -1)
        return res