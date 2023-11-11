class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return list(s) == [w[0] for w in words]