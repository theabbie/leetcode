class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        n = len(persons)
        count = [0] * n
        self.times = times
        self.winner = [-1] * n
        win = (float('-inf'), float('-inf'), -1)
        for i in range(n):
            count[persons[i]] += 1
            win = max(win, (count[persons[i]], times[i], persons[i]))
            self.winner[i] = win[2]

    def q(self, t: int) -> int:
        beg = 0
        end = len(self.times) - 1
        res = -1
        while beg <= end:
            mid = (beg + end) // 2
            if self.times[mid] <= t:
                res = self.winner[mid]
                beg = mid + 1
            else:
                end = mid - 1
        return res