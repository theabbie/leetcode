class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        masks = []
        for i in range(n):
            good = bad = 0
            for j in range(n):
                if statements[i][j] == 0:
                    bad |= 1 << j
                if statements[i][j] == 1:
                    good |= 1 << j
            masks.append((good, bad))
        res = 0
        for mask in range(1 << n):
            bads = 0
            goods = 0
            for i in range(n):
                if mask & (1 << i):
                    goods |= masks[i][0]
                    bads |= masks[i][1]
            if goods | mask == mask and mask & bads == 0:
                res = max(res, mask.bit_count())
        return res