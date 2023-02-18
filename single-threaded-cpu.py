import heapq

class Solution:
    def nexthigher(self, tasks, n, t):
        beg = 0
        end = n - 1
        res = float('inf')
        while beg <= end:
            mid = (beg + end) // 2
            if tasks[mid][0] > t:
                res = tasks[mid][0]
                end = mid - 1
            else:
                beg = mid + 1
        return res
    
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        for i in range(n):
            tasks[i].append(i)
        tasks.sort()
        res = []
        heap = []
        i = 0
        t = 0
        while i < n:
            t = self.nexthigher(tasks, n, t)
            while i < n and tasks[i][0] <= t:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            while len(heap) > 0:
                ptime, idx = heapq.heappop(heap)
                res.append(idx)
                t += ptime
                while i < n and tasks[i][0] <= t:
                    heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                    i += 1
        return res