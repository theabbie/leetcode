class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        free = 0
        res = 0
        for arrival, duration in customers:
            res += max(free - arrival, 0) + duration
            free = max(arrival, free) + duration
        res /= len(customers)
        return res