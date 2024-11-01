from functools import cmp_to_key

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        def cmp(a, b):
            if max(a[1], a[0] + max(b[0], b[1])) > max(b[1], b[0] + max(a[0], a[1])):
                return 1
            return -1
        tasks.sort(key = cmp_to_key(cmp))
        res = 0
        used = 0
        for i in range(len(tasks)):
            res = max(res, used + tasks[i][1])
            used += tasks[i][0]
        return res