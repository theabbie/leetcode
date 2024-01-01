class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num)
        while i >= 1 and int(num[i - 1]) % 2 == 0:
            i -= 1
        return num[:i]