class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        res = 0
        for c in 'MGP':
            j = n - 1
            while j >= 0 and c not in garbage[j]:
                j -= 1
            for i in range(j + 1):
                res += garbage[i].count(c)
                if i < j:
                    res += travel[i]
        return res