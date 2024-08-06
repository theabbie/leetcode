class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        n = len(s)
        res = 0
        order = [("ab", x), ("ba", y)]
        order.sort(key = lambda p: -p[1])
        for ss, cost in order:
            stack = []
            for c in s:
                if stack and stack[-1] + c == ss:
                    stack.pop()
                    res += cost
                else:
                    stack.append(c)
            s = "".join(stack)
        return res