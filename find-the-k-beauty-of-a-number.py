class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        strnum = str(num)
        n = len(strnum)
        ctr = 0
        for i in range(n - k + 1):
            curr = int(strnum[i:i+k])
            if curr != 0 and num % curr == 0:
                ctr += 1
        return ctr