class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        ctr = {}
        for i in range(0, n - 9):
            curr = s[i:i+10]
            ctr[curr] = ctr.get(curr, 0) + 1
        return [patt for patt, freq in ctr.items() if freq > 1]