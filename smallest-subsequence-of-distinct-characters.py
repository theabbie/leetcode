class Solution:
    def smallestSubsequence(self, s: str) -> str:
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
        

# class Solution:
#     def smallestSubsequence(self, s: str) -> str:
#         n = len(s)
#         numdist = len(set(s))
#         smallest = ""
#         paths = [(s[i], [i]) for i in range(n)]
#         while len(paths) > 0:
#             curr, indexes = paths.pop()
#             if smallest:
#                 if curr < smallest and len(curr) == numdist:
#                     smallest = curr
#                     for j in range(indexes[-1] + 1, n):
#                         if s[j] not in curr:
#                             paths.append((curr + s[j], indexes + [j]))
#             elif len(curr) == numdist:
#                 smallest = curr
#         return smallest