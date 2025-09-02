class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        LOG = 1 + n.bit_length()
        jump = [[-1] * LOG for _ in range(n)]
        for i in range(n):
            jump[i][0] = parent[i]
        for k in range(1, LOG):
            for i in range(n):
                if jump[i][k-1] == -1:
                    continue
                jump[i][k] = jump[jump[i][k-1]][k-1]
        self.jump = jump

    def getKthAncestor(self, node: int, k: int) -> int:
        j = 0
        res = node
        while k:
            if k % 2 == 1:
                res = self.jump[res][j]
                if res == -1:
                    break
            j += 1
            k //= 2
        return res