class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        sub = 0
        rem = k
        res = 0
        for el in happiness:
            el = max(el - sub, 0)
            res += el
            sub += 1
            rem -= 1
            if rem == 0:
                break
        return res