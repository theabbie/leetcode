class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse = True)
        n = len(deck)
        cards = deque(list(range(n - 1, -1, -1)))
        res = [-1] * n
        while cards:
            res[cards.pop()] = deck.pop()
            if cards:
                cards.appendleft(cards.pop())
        return res