class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        op = [[0 for i in range(n)] for j in range(2)]
        ctr = []
        for i in range(n):
            if colsum[i] == 2:
                op[0][i] = 1
                upper -= 1
                op[1][i] = 1
                lower -= 1
            elif colsum[i] == 1:
                ctr.append(i)
        if upper >= 0 and lower >= 0 and upper + lower == len(ctr):
            if upper > 0:
                for i in ctr[:upper]:
                    op[0][i] = 1
            if lower > 0:
                for i in ctr[-lower:]:
                    op[1][i] = 1
            return op
        return []