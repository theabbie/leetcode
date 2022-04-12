import bisect

class Solution:
    def mincost(self, days: List[int], costs: List[int], i) -> int:
        n = len(days)
        if i >= n:
            return 0
        if i in self.cache:
            return self.cache[i]
        today = days[i]
        tomorrow = i + 1
        nextweek = bisect.bisect_right(days, today + 6)
        nextmonth = bisect.bisect_right(days, today + 29)
        cost = min(costs[0] + self.mincost(days, costs, tomorrow), costs[1] + self.mincost(days, costs, nextweek), costs[2] + self.mincost(days, costs, nextmonth))
        self.cache[i] = cost
        return cost
    
    def mincostTickets(self, days: List[int], costs: List[int], i = 0) -> int:
        self.cache = {}
        return self.mincost(days, costs, 0)