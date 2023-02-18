class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        negs = []
        pos = []
        for el in nums:
            if el >= 0:
                pos.append(el)
            else:
                negs.append(el)
        negs.sort()
        pos.sort()
        for i in range(min(k, len(negs))):
            negs[i] *= -1
        k -= min(k, len(negs))
        res = sum(negs) + sum(pos)
        if k % 2 != 0:
            a = float('inf') if len(negs) == 0 else negs[-1]
            b = float('inf') if len(pos) == 0 else pos[0]
            res -= 2 * min(a, b)
        return res