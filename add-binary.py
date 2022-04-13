class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = len(a)
        n = len(b)
        if m > n:
            b = "0" * (m - n) + b
        else:
            a = "0" * (n - m) + a
        op = []
        k = max(m, n)
        i = k - 1
        carry = 0
        while i >= 0:
            currval = int(a[i]) + int(b[i]) + carry
            op.append(str(currval % 2))
            carry = currval // 2
            i -= 1
        return "1" * carry + "".join(op[::-1])