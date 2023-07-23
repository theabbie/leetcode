class FenwickTree:
    def __init__(self, x):
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        pos = []
        for i in range(n):
            pos.append((times[i][0], 1, i))
            pos.append((times[i][1], -1, i))
        pos.sort()
        used = FenwickTree([0] * (n + 1))
        seat = {}
        for t, inc, friend in pos:
            if inc == 1:
                beg = 0
                end = n
                chair = end
                while beg <= end:
                    mid = (beg + end) // 2
                    if used.query(mid + 1) < mid + 1:
                        chair = mid
                        end = mid - 1
                    else:
                        beg = mid + 1
                used.update(chair, 1)
                seat[friend] = chair
            else:
                used.update(seat[friend], -1)
        return seat[targetFriend]