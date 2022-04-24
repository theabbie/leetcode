from collections import defaultdict
import bisect

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        times = defaultdict(int)
        for s, e in flowers:
            times[s] += 1
            times[e + 1] -= 1
        timekeys = sorted(times.keys())
        prefix = [0]
        for t in timekeys:
            prefix.append(prefix[-1] + times[t])
        answer = []
        for p in persons:
            i = bisect.bisect_right(timekeys, p)
            answer.append(prefix[min(i, len(prefix) - 1)])
        return answer