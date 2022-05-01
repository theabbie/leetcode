class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        pos = {}
        minDiff = float('inf')
        for i in range(n):
            if cards[i] in pos:
                minDiff = min(minDiff, i - pos[cards[i]] + 1)
            pos[cards[i]] = i
        if minDiff == float('inf'):
            return -1
        return minDiff