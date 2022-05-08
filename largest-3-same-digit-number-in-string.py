class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        i = 0
        mnum = float('-inf')
        while i < n:
            ctr = 1
            while i < n - 1 and num[i] == num[i + 1]:
                i += 1
                ctr += 1
            i += 1
            if ctr >= 3:
                mnum = max(mnum, int(num[i - 1]))
        if mnum == float('-inf'):
            return ""
        return str(mnum) * 3