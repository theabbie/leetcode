class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = True
        for bracket in s:
            if bracket == '(':
                stack.append(bracket)
            elif bracket == ')':
                if len(stack) > 0:
                    if stack.pop() + bracket != '()':
                        valid = False
                        break
                else:
                    valid = False
                    break
        if len(stack) > 0:
            valid = False
        return valid
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)
        paths = [("", 0, 0)]
        btoi = { '(': 1, ')': -1 }
        i = 0
        mindels = n
        op = set()
        visited = set()
        while i < len(paths):
            curr, j, currctr = paths[i]
            if j == n:
                if self.isValid(curr):
                    if n - len(curr) < mindels:
                        mindels = n - len(curr)
                        op = { curr }
                    elif n - len(curr) == mindels:
                        op.add(curr)
            if j < n and j - len(curr) <= mindels:
                nctr = currctr + btoi.get(s[j], 0)
                if nctr >= 0 and (curr + s[j], j + 1) not in visited:
                    visited.add((curr + s[j], j + 1))
                    paths.append((curr + s[j], j + 1, nctr))
                if s[j] == '(' or s[j] == ')' and (curr, j + 1) not in visited:
                    visited.add((curr, j + 1))
                    paths.append((curr, j + 1, currctr))
            i += 1
        return list(op)