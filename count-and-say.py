class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = self.countAndSay(n - 1)
        n = len(prev)
        op = ""
        i = 0
        while i < n:
            ctr = 1
            while i < n - 1 and prev[i] == prev[i + 1]:
                ctr += 1
                i += 1
            i += 1
            op += str(ctr) + prev[i - 1]
        return op