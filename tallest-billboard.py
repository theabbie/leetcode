from collections import defaultdict

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = defaultdict(int)
        dp[0] = 0
        for r in rods:
            curr = defaultdict(int)
            for el in dp:
                curr[el] = dp[el]
            for diff, longer in dp.items():
                smaller = longer - diff
                curr[diff + r] = max(curr[diff + r], longer + r)
                currdiff = abs(smaller + r - longer)
                currlonger = max(smaller + r, longer)
                curr[currdiff] = max(curr[currdiff], currlonger)
            dp = curr
        return dp[0]