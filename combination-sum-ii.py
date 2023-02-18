from collections import deque

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        q = deque([(target, -1, 0)])
        res = []
        while len(q) > 0:
            rem, i, used = q.pop()
            if rem == 0:
                res.append([candidates[x] for x in range(n) if used & (1 << x)])
            if rem > 0:
                for j in range(i + 1, n):
                    if j == 0 or j == i + 1 or candidates[j] != candidates[j - 1]:
                        q.appendleft((rem - candidates[j], j, used | 1 << j))
        return res