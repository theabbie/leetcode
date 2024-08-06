from collections import *

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        cnt = lambda x: str(x) if x > 1 else ""
        rnd = 2
        def tokentype(x):
            nonlocal rnd
            if x.isalpha() and x.isupper():
                rnd += 1
                return rnd
            if x.isalpha() and x.islower():
                return 1
            if x.isdigit():
                return 2
            if x == '(':
                rnd += 1
                return rnd
            rnd += 1
            return rnd
        tokens = []
        i = 0
        while i < n:
            ctr = 1
            while i < n - 1 and tokentype(formula[i]) == tokentype(formula[i + 1]):
                ctr += 1
                i += 1
            if tokentype(formula[i]) == 1:
                tokens.append(tokens.pop() + formula[i-ctr+1:i+1])
            elif tokentype(formula[i]) == 2:
                tokens.append(int(formula[i-ctr+1:i+1]))
            else:
                tokens.append(formula[i-ctr+1:i+1])
            i += 1
        stack = [Counter()]
        i = 0
        def next():
            if i >= len(tokens):
                return False
            return True
        def peek():
            return tokens[i]
        def consume():
            nonlocal i
            i += 1
            return tokens[i - 1]
        while next():
            curr = consume()
            if curr == '(':
                stack.append(Counter())
            elif curr == ')':
                mul = 1
                if next() and str(peek()).isdigit():
                    mul = consume()
                for x in stack[-1]:
                    stack[-1][x] *= mul
                if len(stack) > 1:
                    x = stack.pop()
                    stack[-1] += x
            elif str(curr).isalpha():
                atom = curr
                mul = 1
                if next() and str(peek()).isdigit():
                    mul = consume()
                stack[-1] += Counter({atom: mul})
        while len(stack) > 1:
            x = stack.pop()
            stack[-1] += x
        res = stack.pop()
        return "".join(f"{atom}{cnt(res[atom])}" for atom in sorted(res))