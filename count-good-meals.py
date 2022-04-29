from collections import Counter

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        deliciousness = Counter(deliciousness)
        ctr = 0
        for i in range(22):
            total = 1 << i
            for d in deliciousness:
                if total - d in deliciousness:
                    if 2 * d != total:
                        ctr += deliciousness[d] * deliciousness[total - d] / 2
                    else:
                        ctr += deliciousness[d] * (deliciousness[d] - 1) // 2
        return int(ctr) % (10 ** 9 + 7)