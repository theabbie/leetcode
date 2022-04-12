class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[k - 1] = 0
        for i in range(n - 1):
            for a, b, d in times:
                if dist[b - 1] > dist[a - 1] + d:
                    dist[b - 1] = dist[a - 1] + d
        delay = max(dist)
        if delay == float('inf'):
            return -1
        return delay