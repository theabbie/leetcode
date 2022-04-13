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
        brackets = {
            '(': 1,
            ')': -1
        }
        numstack = []
        opstack = []
        chunk = ""
        latestOpenBracket = True
        for c in s:
            if c == " " or c in precedence or c in brackets:
                if len(chunk) > 0:
                    numstack.append(int(chunk))
                    chunk = ""
                if c in brackets:
                    if brackets[c] == 1:
                        opstack.append('(')
                        latestOpenBracket = True
                    elif brackets[c] == -1:
                        latestOpenBracket = False
                        while opstack[-1] != '(':
                            currop = opstack.pop()
                            b = numstack.pop()
                            a = numstack.pop()
                            res = self.eval(a, currop, b)
                            numstack.append(res)
                        opstack.pop()
                elif c in precedence:
                    if latestOpenBracket:
                        numstack.append(0)
                    while len(opstack) > 0 and precedence.get(opstack[-1], -1) >= precedence[c]:
                        currop = opstack.pop()
                        b = numstack.pop()
                        a = numstack.pop()
                        res = self.eval(a, currop, b)
                        numstack.append(res)
                    opstack.append(c)
                    latestOpenBracket = False
            else:
                chunk += c
                latestOpenBracket = False
        while len(opstack) > 0:
            currop = opstack.pop()
            b = numstack.pop()
            a = numstack.pop()
            res = self.eval(a, currop, b)
            numstack.append(res)
        return numstack[0]