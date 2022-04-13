class Solution:
    def eval(self, a, op, b):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '/':
            return int(a / b)
        elif op == '*':
            return a * b
    
    def calculate(self, s: str) -> int:
        s += " "
        precedence = {
            '*': 1,
            '/': 1,
            '+': 0,
            '-': 0
        }
        numstack = []
        opstack = []
        chunk = ""
        for c in s:
            if c == " " or c in precedence:
                if len(chunk) > 0:
                    numstack.append(int(chunk))
                    chunk = ""
                if c in precedence:
                    while len(opstack) > 0 and precedence[opstack[-1]] >= precedence[c]:
                        currop = opstack.pop()
                        b = numstack.pop()
                        a = numstack.pop()
                        res = self.eval(a, currop, b)
                        numstack.append(res)
                    opstack.append(c)
            else:
                chunk += c
        while len(opstack) > 0:
            currop = opstack.pop()
            b = numstack.pop()
            a = numstack.pop()
            res = self.eval(a, currop, b)
            numstack.append(res)
        return numstack[0]