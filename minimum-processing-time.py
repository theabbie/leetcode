from sortedcontainers import SortedList

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        n = len(processorTime)
        processorTime.sort()
        tasks.sort(reverse = True)
        res = 0
        for i in range(n):
            for j in range(4 * i, 4 * i + 4):
                res = max(res, processorTime[i] + tasks[j])
        return res