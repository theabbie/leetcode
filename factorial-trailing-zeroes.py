class Solution:
    def trailingZeroes(self, n: int) -> int:
        ctr = [0, 0]
        for i in range(1, n + 1):
            curr = i
            while curr % 2 == 0:
                ctr[0] += 1
                curr = curr // 2
            while curr % 5 == 0:
                ctr[1] += 1
                curr = curr // 5
        return min(ctr)