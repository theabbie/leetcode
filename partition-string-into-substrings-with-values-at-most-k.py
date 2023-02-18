class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        n = len(s)
        v = 0
        res = 1
        for c in s:
            if 10 * v + int(c) > k:
                res += 1
                v = int(c)
                if v > k:
                    return -1
            else:
                v = 10 * v + int(c)
        return res