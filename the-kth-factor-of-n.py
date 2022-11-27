class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i = 1
        res = -1
        ctr = 0
        rev = []
        fw = []
        while i * i <= n:
            if n % i == 0:
                fw.append(i)
                if i * i != n:
                    rev.append(n // i)
            i += 1
        if k <= len(fw):
            return fw[k - 1]
        if k - len(fw) <= len(rev):
            return rev[len(rev) - k + len(fw)]
        return -1