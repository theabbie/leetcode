class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while len(stack) > 0 and c < stack[-1] and k:
                stack.pop()
                k -= 1
            stack.append(c)
        while k:
            stack.pop()
            k -= 1
        i = 0
        while i < len(stack) and stack[i] == "0":
            i += 1
        if i >= len(stack):
            return "0"
        return "".join(stack[i:])