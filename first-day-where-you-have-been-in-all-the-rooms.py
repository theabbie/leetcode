class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        M = 10 ** 9 + 7
        start = [0] * n
        end = [0] * n
        end[0] = 1
        for i in range(1, n):
            start[i] = end[i - 1] + 1
            end[i] = 2 * start[i] - start[nextVisit[i]] + 1
            start[i] %= M
            end[i] %= M
        return start[-1]