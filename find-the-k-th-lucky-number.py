class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        l = 1
        while k > pow(2, l):
            k -= pow(2, l)
            l += 1
        return "".join("4" if c == "0" else "7" for c in ('{:0' + str(l) + 'b}').format(k - 1))