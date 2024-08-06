class Solution:
    def minFlips(self, target: str) -> int:
        n = len(target)
        res = 0
        flip = False
        for i in range(n):
            curr = '1' if flip else '0'
            if curr != target[i]:
                res += 1
                flip = not flip
        return res