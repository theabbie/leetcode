class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        SQRT = 1
        while (SQRT + 1) * (SQRT + 1) < n:
            SQRT += 1
        p = [-1 for i in range(n)]
        for i in range(n):
            curr = i
            for _ in range(SQRT):
                curr = parent[curr] if curr != -1 else -1
            p[i] = curr
        self.parent = parent
        self.p = p
        self.SQRT = SQRT

    def getKthAncestor(self, node: int, k: int) -> int:
        i = 0
        while i < k:
            if i + self.SQRT <= k:
                node = self.p[node]
                i += self.SQRT
            else:
                node = self.parent[node]
                i += 1
            if node == -1:
                break
        return node