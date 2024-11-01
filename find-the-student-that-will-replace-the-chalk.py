class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        k %= s
        i = 0
        while chalk[i] <= k:
            k -= chalk[i]
            i += 1
        return i