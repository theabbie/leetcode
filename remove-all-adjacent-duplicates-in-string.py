class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if len(stack) == 0 or c != stack[-1][0]:
                stack.append([c, 1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == 2:
                    stack.pop()
        return "".join([c[0] * c[1] for c in stack])