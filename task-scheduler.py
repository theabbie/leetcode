from collections import *

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t = 0
        available = defaultdict(lambda: -1)
        ctr = Counter(tasks)
        while ctr:
            best = (0, "")
            for c in ctr:
                if available[c] <= t:
                    best = max(best, (ctr[c], c))
            t += 1
            if best[0] == 0:
                continue
            ctr[best[1]] -= 1
            if ctr[best[1]] == 0:
                del ctr[best[1]]
            available[best[1]] = t + n
        return t