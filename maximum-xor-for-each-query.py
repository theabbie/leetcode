class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        res = []
        pw = [1] * 21
        for i in range(1, 21):
            pw[i] = 2 * pw[i - 1]
        x = 0
        for el in nums:
            x ^= el
            curr = 0
            for b in range(maximumBit - 1, -1, -1):
                if not x & pw[b]:
                    curr |= pw[b]
            res.append(curr)
        res.reverse()
        return res