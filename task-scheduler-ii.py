class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        t = 0
        prev = {}
        for task in tasks:
            if task in prev:
                t += max(space - t + prev[task] + 1, 0)
            prev[task] = t
            t += 1
        return t