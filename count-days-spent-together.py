class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        start = max(arriveAlice, arriveBob)
        sm, sd = map(int, start.split("-"))
        end = min(leaveAlice, leaveBob)
        em, ed = map(int, end.split("-"))
        res = 0
        for m in range(sm + 1, em):
            res += days[m - 1]
        if em > sm:
            res += days[sm - 1] - sd + ed + 1
        elif em == sm:
            res += max(ed - sd + 1, 0)
        return res