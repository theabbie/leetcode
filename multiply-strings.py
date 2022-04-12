class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        if m < n:
            num1 = "0" * (n - m) + num1
        else:
            num2 = "0" * (m - n) + num2
        carry = 0
        i = max(m, n) - 1
        op = ""
        while i >= 0:
            val = carry + int(num1[i]) + int(num2[i])
            op = str(val % 10) + op
            carry = val // 10
            i -= 1
        if carry > 0:
            op = "1" + op
        return op
    
    def mulNtimes(self, num, n):
        op = "0"
        for _ in range(n):
            op = self.addStrings(op, num)
        return op
    
    def multiply(self, num1: str, num2: str) -> str:
        op = "0"
        n = len(num2)
        for i in range(n):
            curr = self.mulNtimes(num1, int(num2[n - i - 1]))
            if curr != "0":
                curr += "0" * i
            op = self.addStrings(op, curr)
        return op