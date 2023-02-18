from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        pos = defaultdict(list)
        for i in range(n):
            pos[arr[i]].append(i)
        q = deque([(0, 0)])
        v = {0}
        pos[arr[0]].remove(0)
        res = float('inf')
        while len(q) > 0:
            curr, d = q.pop()
            if curr == n - 1:
                res = min(res, d)
            for j in pos[arr[curr]] + [curr - 1, curr + 1]:
                if 0 <= j < n and j != curr and j not in v:
                    v.add(j)
                    pos[arr[j]].remove(j)
                    q.appendleft((j, d + 1))
        return res