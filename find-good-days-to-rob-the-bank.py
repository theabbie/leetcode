class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        mdec = [1] * n
        minc = [1] * n
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                mdec[i] = 1 + mdec[i - 1]
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                minc[i] = 1 + minc[i + 1]
        res = []
        for i in range(time, n - time):
            if mdec[i] >= time + 1 and minc[i] >= time + 1:
                res.append(i)
        return res