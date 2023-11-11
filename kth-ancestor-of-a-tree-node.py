class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        LOG = 1 + len("{:0b}".format(n + 1))
        p = [[-1] * LOG for _ in range(n)]
        for l in range(LOG):
            for i in range(n):
                if l == 0:
                    p[i][l] = parent[i]
                elif p[i][l - 1] != -1:
                    p[i][l] = p[p[i][l - 1]][l - 1]
        self.p = p

    def getKthAncestor(self, node: int, k: int) -> int:
        res = node
        pw = 0
        while k:
            if k & 1:
                res = self.p[res][pw]
                if res == -1:
                    return -1
            k //= 2
            pw += 1
        return res