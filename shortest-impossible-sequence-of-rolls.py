class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        res = []
        n = len(rolls)
        subs = set()
        for i in range(n):
            subs.add(rolls[i])
            if len(subs) == k:
                res.append(rolls[i])
                subs.clear()
        for j in range(1, k + 1):
            if j not in subs:
                res.append(j)
                return len(res)
        return len(res)