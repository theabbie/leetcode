class Solution:
    def sumOfPower(self, arr):
        n = len(arr)
        M = 10 ** 9 + 7
        pw = [1] * (n + 1)
        for i in range(1, n + 1):
            pw[i] = 2 * pw[i - 1]
            pw[i] %= M
        arr.sort()
        res = 0
        s = 0
        for i in range(n - 1, -1, -1):
            res += arr[i] * arr[i] * arr[i]
            res += arr[i] * s * pow(pw[i + 1], M - 2, M)
            res %= M
            s += pw[i] * arr[i] * arr[i]
            s %= M
        return res