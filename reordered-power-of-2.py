class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        l = len(str(n))
        k = 0
        currlen = len(str(1 << k))
        sortedval = sorted(str(n))
        while currlen <= l:
            if currlen == l:
                if sorted(str(1 << k)) == sortedval:
                    return True
            k += 1
            currlen = len(str(1 << k))
        return False