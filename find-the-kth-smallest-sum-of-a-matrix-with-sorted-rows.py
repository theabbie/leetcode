import heapq

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        n = len(mat[0])
        pos = [0] * m
        s = 0
        for i in range(m):
            s += mat[i][pos[0]]
        v = {tuple(pos)}
        heap = [(s, pos)]
        rem = k
        while heap:
            s, pos = heapq.heappop(heap)
            rem -= 1
            if rem == 0:
                return s
            for i in range(m):
                if pos[i] + 1 < n:
                    newpos = pos[:]
                    newpos[i] += 1
                    news = s - mat[i][pos[i]] + mat[i][pos[i] + 1]
                    if tuple(newpos) not in v:
                        v.add(tuple(newpos))
                        heapq.heappush(heap, (news, newpos))