class Solution:
    def getRowState(self, poured, query_row):
        if query_row == 0:
            return [poured]
        prev = self.getRowState(poured, query_row - 1)
        curr = [0] * (query_row + 1)
        for i in range(query_row):
            if prev[i] > 1:
                extra = (prev[i] - 1) / 2
                curr[i] += extra
                curr[i + 1] += extra
        return curr
    
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        state = self.getRowState(poured, query_row)
        return min(state[query_glass], 1)