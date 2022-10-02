class Solution:
    def count(self, pos, cnt, tight, nonz, num, d, K, dp):
        if pos == len(num):
            if cnt == K:
                return 1
            return 0
        if dp[pos][cnt][tight][nonz] != -1:
            return dp[pos][cnt][tight][nonz]
        ans = 0
        limit = 9 if tight else num[pos]
        for dig in range(limit + 1):
            currCnt = cnt
            if dig == d:
                if d != 0 or not d and nonz:
                    currCnt += 1
            currTight = tight
            if dig < num[pos]:
                currTight = 1
            ans += self.count(pos + 1, currCnt, currTight, (nonz or dig != 0), num, d, K, dp)
        dp[pos][cnt][tight][nonz] = ans
        return dp[pos][cnt][tight][nonz]
    
    def countDigitOne(self, n: int) -> int:
        digits = []
        while n:
            digits.append(n % 10)
            n //= 10
        digits.reverse()
        res = 0
        for k in range(1, 1 + len(digits)):
            dp = [[[[-1, -1] for i in range(2)] for j in range(10)] for k in range(10)]
            res += k * self.count(0, 0, 0, 0, digits, 1, k, dp)
        return res