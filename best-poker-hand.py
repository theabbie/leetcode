from collections import defaultdict

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        n = len(ranks)
        ctr = defaultdict(int)
        for r in ranks:
            ctr[r] += 1
        if len(set(suits)) == 1:
            return "Flush"
        for r in sorted(ctr.values(), reverse = True):
            if r >= 3:
                return "Three of a Kind"
            if r == 2:
                return "Pair"
        return "High Card"