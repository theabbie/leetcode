class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        ctr = [0, 0]
        swaps = [0, 0]
        for i in range(n):
            d = int(s[i])
            swaps[int(d == i % 2)] += 1
            ctr[d] += 1
        if abs(ctr[1] - ctr[0]) > 1:
            return -1
        swaps.sort()
        if swaps[0] % 2 == 0:
            return swaps[0] // 2
        return swaps[1] // 2