class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        s = [0] * n
        res = float('-inf')
        for i in range(n - 1, -1, -1):
            s[i % k] += energy[i]
            res = max(res, s[i % k])
        return res