class Solution:
    def maximumSwap(self, num: int) -> int:
        currmax = num
        d = list(str(num))
        n = len(d)
        for i in range(n - 1):
            j = max([(int(d[k]), k) for k in range(i + 1, n)])[1]
            if int(d[j]) > int(d[i]):
                d[i], d[j] = d[j], d[i]
                break
        currmax = max(currmax, int("".join(d)))
        return currmax