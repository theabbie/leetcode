class Solution:
    def getLucky(self, s: str, k: int) -> int:
        op = ""
        for c in s:
            op += str(ord(c) - ord('a') + 1)
        for i in range(k):
            op = str(sum([int(d) for d in op]))
        return int(op)