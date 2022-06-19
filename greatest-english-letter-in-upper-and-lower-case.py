class Solution:
    def greatestLetter(self, s: str) -> str:
        lower = set()
        upper = set()
        for c in s:
            if c.islower():
                lower.add(c)
            if c.isupper():
                upper.add(c.lower())
        common = set.intersection(lower, upper)
        if len(common) == 0:
            return ""
        return max(common).upper()