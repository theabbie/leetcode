class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        bigger = {}
        smaller = {}
        for i in range(n):
            for j in range(i + 1, n):
                if rating[i] > rating[j]:
                    smaller[i] = smaller.get(i, []) + [j]
                if rating[i] < rating[j]:
                    bigger[i] = bigger.get(i, []) + [j]
        total = 0
        for a in bigger:
            for b in bigger.get(a, []):
                total += len(bigger.get(b, []))
        for a in smaller:
            for b in smaller.get(a, []):
                total += len(smaller.get(b, []))
        return total