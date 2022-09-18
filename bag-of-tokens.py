class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)
        tokens.sort()
        res = 0
        i = 0
        j = n - 1
        while i <= j:
            if power >= tokens[i]:
                res += 1
                power -= tokens[i]
                i += 1
            elif res > 0 and i + 1 < j:
                res -= 1
                power += tokens[j]
                j -= 1
            else:
                break
        return res