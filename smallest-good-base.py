class Solution:
    def getNum(self, base, l):
        val = 0
        for _ in range(l):
            val = base * val + 1
        return val
    
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        for l in range(len("{:b}".format(n)), 1, -1):
            beg = 2
            end = n - 1
            while beg <= end:
                mid = (beg + end) // 2
                val = self.getNum(mid, l)
                if val == n:
                    return str(mid)
                elif beg == end:
                    break
                elif val < n:
                    beg = mid + 1
                else:
                    end = mid