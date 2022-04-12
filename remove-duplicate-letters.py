class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        used = set()
        stack = []
        for i, c in enumerate(s):
            if c in used:
                continue
            while len(stack) > 0 and s[stack[-1]] > c and i < lastIndex[s[stack[-1]]]:
                curr = stack.pop()
                if s[curr] in used:
                    used.remove(s[curr])
            stack.append(i)
            used.add(c)
        return "".join(s[i] for i in stack)