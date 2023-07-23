class Solution:
    def longest(self, arr, k):
        n = len(arr)
        p = [0]
        for el in arr:
            p.append(p[-1] + el)
        res = 0
        i = 0
        zeroes = lambda x, y: y - x + 1 - p[y + 1] + p[x]
        for j in range(n):
            while i < j and zeroes(i, j) > k:
                i += 1
            if zeroes(i, j) <= k:
                res = max(res, j - i + 1)
        return res
    
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        return max(self.longest([int(c == 'T') for c in answerKey], k), self.longest([int(c == 'F') for c in answerKey], k))