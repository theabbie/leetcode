class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        res = 0
        sub = 0
        rem = k
        for el in happiness:
            el = max(el - sub, 0)
            if rem > 0:
                res += el
                rem -= 1
                sub += 1
            else:
                break
        return res