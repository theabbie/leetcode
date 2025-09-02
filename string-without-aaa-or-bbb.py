class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
        n = a + b
        while len(res) < n:
            apos = True
            bpos = True
            if len(res) >= 2 and res[-1] == res[-2] == 'a':
                apos = False
            if len(res) >= 2 and res[-1] == res[-2] == 'b':
                bpos = False
            if apos and bpos:
                if a >= b:
                    res.append('a')
                    a -= 1
                else:
                    res.append('b')
                    b -= 1
            elif apos:
                res.append('a')
                a -= 1
            elif bpos:
                res.append('b')
                b -= 1
        return "".join(res)