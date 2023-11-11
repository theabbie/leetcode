class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        ind = lambda x: ord(x) - ord('A')
        res = [1] * n
        last = [-1] * 26
        for i in range(n):
            res[i] *= i - last[ind(s[i])]
            last[ind(s[i])] = i
        last = [n] * 26
        for i in range(n - 1, -1, -1):
            res[i] *= last[ind(s[i])] - i
            last[ind(s[i])] = i
        return sum(res)