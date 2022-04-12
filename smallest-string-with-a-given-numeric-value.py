class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        k -= n
        op = [0] * n
        i = n - 1
        while k > 0:
            diff = min(k, 25 - op[i])
            op[i] += diff
            k -= diff
            i -= 1
        return "".join(chr(ord('a') + i) for i in op)