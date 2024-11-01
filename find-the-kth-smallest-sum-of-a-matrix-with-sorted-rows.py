import heapq

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        n = len(mat[0])
        pos = [0] * m
        s = 0
        for i in range(m):
            s += mat[i][pos[i]]
        heap = [(s, [0] * m)]
        v = set()
        for _ in range(k):
            currs, poses = heapq.heappop(heap)
            s = currs
            for i in range(m):
                if poses[i] + 1 < n:
                    news = currs - mat[i][poses[i]] + mat[i][poses[i] + 1]
                    poses[i] += 1
                    pt = tuple(poses)
                    if pt not in v:
                        v.add(pt)
                        heapq.heappush(heap, (news, poses[:]))
                    poses[i] -= 1
        return s