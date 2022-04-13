class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in { '+', '-', '*', '/' }:
                op2 = stack.pop()
                op1 = stack.pop()
                if t == '+':
                    stack.append(op1 + op2)
                elif t == '-':
                    stack.append(op1 - op2)
                elif t == '*':
                    stack.append(op1 * op2)
                elif t == '/':
                    stack.append(int(op1 / op2))
            else:
                stack.append(int(t))
        return stack.pop()