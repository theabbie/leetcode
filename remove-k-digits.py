class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if n == k:
            return "0"
        stack = []
        for i in range(n):
            if len(stack) == 0:
                stack.append(num[i])
            else:
                while len(stack) > 0 and int(num[i]) < int(stack[-1]) and len(stack) >= i - k + 1:
                    stack.pop()
                if len(stack) == 0 or len(stack) < n - k:
                    stack.append(num[i])
        return str(int("".join(stack)))