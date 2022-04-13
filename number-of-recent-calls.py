import bisect

class RecentCounter:

    def __init__(self):
        self.times = []

    def ping(self, t: int) -> int:
        bisect.insort(self.times, t)
        n = len(self.times)
        return n - bisect.bisect_left(self.times, t - 3000)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)