class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.cache = {}
        def get(node, p):
            if p == 0:
                return parent[node]
            if (node, p) in self.cache:
                return self.cache[(node, p)]
            half = get(node, p - 1)
            self.cache[(node, p)] = get(half, p - 1) if half != -1 else -1
            return self.cache[(node, p)]
        self.get = get

    def getKthAncestor(self, node: int, k: int) -> int:
        res = node
        p = 0
        while k:
            if k & 1:
                res = self.get(res, p)
                if res == -1:
                    break
            p += 1
            k //= 2
        return res