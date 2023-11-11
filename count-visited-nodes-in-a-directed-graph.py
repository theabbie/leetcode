class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        res = [0] * n
        v = set()
        cycles = {}
        for node in range(n):
            i = 0
            pos = {}
            curr = []
            while node != -1 and node not in v:
                pos[node] = i
                curr.append(node)
                v.add(node)
                node = edges[node]
                i += 1
            if node != -1 and node in pos:
                for j in range(1, i - pos[node] + 1):
                    res[curr[-j]] = i - pos[node]
        LOG = 1 + len("{:0b}".format(n + 1))
        parent = [[edges[i]] * LOG for i in range(n)]
        for d in range(1, LOG):
            for i in range(n):
                parent[i][d] = parent[parent[i][d - 1]][d - 1]
        for i in range(n):
            if res[i] != 0:
                continue
            curr = i
            visited = 1
            for k in range(LOG - 1, -1, -1):
                if res[parent[curr][k]] == 0:
                    curr = parent[curr][k]
                    visited += 1 << k
            visited += res[edges[curr]]
            res[i] = visited
        return res