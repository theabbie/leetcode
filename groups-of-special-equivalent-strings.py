class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def convert(s):
            n = len(s)
            s = list(s)
            v = [[], []]
            for i in range(n):
                v[i % 2].append(s[i])
            v[0].sort(reverse = True)
            v[1].sort(reverse = True)
            for i in range(n):
                s[i] = v[i % 2].pop()
            return "".join(s)
        return len(set(convert(s) for s in words))