class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = mean * (m + n)
        rem = total - sum(rolls)
        res = [rem // n] * n
        k = rem % n
        for i in range(k):
            res[i] += 1
        if max(res) > 6 or min(res) < 1:
            return []
        return res