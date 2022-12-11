from collections import deque, defaultdict
import heapq

class Solution:
    def match(self, a, b):
        m = len(a)
        n = len(b)
        for i in range(min(m, n), 0, -1):
            if a[-i:] == b[:i]:
                return i
        return 0
    
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        if n == 1:
            return "".join(words)
        match = [[0] * n for _ in range(n)]
        for i in range(n):
            match[i][i] = len(words[i])
            for j in range(i + 1, n):
                match[i][j] = self.match(words[i], words[j])
                match[j][i] = self.match(words[j], words[i])
        heap = []
        dist = defaultdict(lambda: float('inf'))
        parent = {}
        for i in range(n):
            heapq.heappush(heap, (0, i, 1 << i))
            dist[(i, 1 << i)] = len(words[i])
        while len(heap) > 0:
            d, i, mask = heapq.heappop(heap)
            for j in range(n):
                if i != j and dist[(j, mask | 1 << j)] > dist[(i, mask)] + len(words[j]) - match[i][j]:
                    dist[(j, mask | 1 << j)] = dist[(i, mask)] + len(words[j]) - match[i][j]
                    heapq.heappush(heap, (dist[(j, mask | 1 << j)], j, mask | 1 << j))
                    parent[(j, mask | 1 << j)] = (i, mask)
        mlen = float('inf')
        for i in range(n):
            mlen = min(mlen, dist[(i, (1 << n) - 1)])
        seq = []
        for el in parent:
            if el[1] + 1 == 1 << n and dist[el] == mlen:
                path = [el[0]]
                while el in parent:
                    el = parent[el]
                    path.append(el[0])
                seq = path[::-1]
                break
        res = []
        for i in range(len(seq) - 1):
            res.append(words[seq[i]][:len(words[seq[i]]) - match[seq[i]][seq[i+1]]])
        res.append(words[seq[-1]])
        return "".join(res)