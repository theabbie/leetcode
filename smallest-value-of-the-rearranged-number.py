class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return num
        negative = num < 0
        num = abs(num)
        num = list(str(num))
        if negative:
            return -int("".join(sorted(num, reverse = True)))
        minDigit = min(d for d in num if d != "0")
        num.remove(minDigit)
        return int(minDigit + "".join(sorted(num)))