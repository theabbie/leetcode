class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        total = 0
        currmin = float('inf')
        currmax = float('-inf')
        for i in range(n):
            currmin = min(currmin, salary[i])
            currmax = max(currmax, salary[i])
            total += salary[i]
        return (total - currmin - currmax) / (n - 2)