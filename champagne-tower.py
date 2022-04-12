class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0:
            return 0
        state = [poured]
        k = 0
        while True:
            n = len(state)
            newstate = [0] * (n + 1)
            spilled = False
            for i in range(n):
                if state[i] > 1:
                    spilled = True
                    newstate[i] += (state[i] - 1) / 2
                    newstate[i + 1] += (state[i] - 1) / 2
                    state[i] = 1
            if k == query_row:
                return state[query_glass]
            if not spilled:
                break
            state = newstate
            k += 1
        return 0