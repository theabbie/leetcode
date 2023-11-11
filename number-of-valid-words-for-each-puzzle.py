from collections import Counter

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        ctr = Counter()
        for w in words:
            mask = 0
            for c in w:
                mask |= 1 << (ord(c) - ord('a'))
            ctr[mask] += 1
        res = []
        for w in puzzles:
            REQ = (1 << (ord(w[0]) - ord('a')))
            curr = 0
            mask = 0
            for c in w:
                mask |= 1 << (ord(c) - ord('a'))
            s = mask
            while s:
                if s & REQ:
                    curr += ctr[s]
                s = (s - 1) & mask
            res.append(curr)
        return res