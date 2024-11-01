class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        n = len(expression)
        stack = []
        i = 0
        while i < n:
            if i < n - 1 and expression[i:i+2] in {"!(", "&(", "|("}:
                stack.append(expression[i:i+2])
                i += 2
            elif expression[i] == ')':
                vals = []
                while stack[-1] not in {"!(", "&(", "|("}:
                    vals.append(stack.pop())
                op = stack.pop()[0]
                if op == '!':
                    stack.append(not vals[0])
                if op == '&':
                    stack.append(False not in vals)
                if op == '|':
                    stack.append(True in vals)
                i += 1
            elif expression[i] == 'f':
                stack.append(False)
                i += 1
            elif expression[i] == 't':
                stack.append(True)
                i += 1
            else:
                i += 1
        return stack.pop()