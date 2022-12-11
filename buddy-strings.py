class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        m = len(s)
        n = len(goal)
        if m != n:
            return False
        sdiff = []
        gdiff = []
        eq = False
        seen = set()
        for i in range(n):
            if s[i] != goal[i]:
                sdiff.append(s[i])
                gdiff.append(goal[i])
            else:
                if s[i] in seen:
                    eq = True
                seen.add(s[i])
        if s == goal:
            return eq
        if not len(sdiff) == len(gdiff) == 2:
            return False
        return sorted(sdiff) == sorted(gdiff)