class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for w in words:
            res.extend(w.split(separator))
        return [s for s in res if len(s) > 0]