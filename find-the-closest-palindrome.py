class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if n == '9' * len(n) and n != '9':
            return '1' + ('0' * (len(n) - 1)) + '1'
        if n == '1' + '0' * (len(n) - 1) and len(n) > 1:
            return '9' * (len(n) - 1)
        if n == '11':
            return '9'
        res = (float('inf'), float('inf'))
        nval = int(n)
        if len(n) > 2:
            val = int('9' * (len(n) - 1))
            res = min(res, (abs(val - nval), val))
        if len(n) % 2 == 0:
            k = len(n) // 2 - 1
            for x in range(10):
                val = int(n[:k] + str(x) * 2 + n[:k][::-1])
                if val != nval:
                    res = min(res, (abs(val - nval), val))
            if len(n) >= 4:
                k = len(n) // 2 - 2
                for x in range(10, 100):
                    val = int(n[:k] + str(x) + str(x)[::-1] + n[:k][::-1])
                    if val != nval:
                        res = min(res, (abs(val - nval), val))
            return str(res[1])
        k = len(n) // 2
        for x in range(10):
            val = int(n[:k] + str(x) + n[:k][::-1])
            if val != nval:
                res = min(res, (abs(val - nval), val))
        return str(res[1])