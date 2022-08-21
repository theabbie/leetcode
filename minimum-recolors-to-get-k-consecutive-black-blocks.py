class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        res = float('inf')
        for i in range(n - k + 1):
            ctr = 0
            for j in range(i, i + k):
                if blocks[j] == "W":
                    ctr += 1
            res = min(res, ctr)
        return res