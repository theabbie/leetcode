class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse = True)
        tasks.sort()
        res = 0
        for i in range(len(processorTime)):
            res = max(res, processorTime[i] + tasks[3 + i * 4])
        return res