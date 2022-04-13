class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            num = abs(num)
            num = list(str(num))
            return -int("".join(sorted(num, reverse = True)))
        num = abs(num)
        num = list(str(num))
        ds = [d for d in num if d != "0"]
        minDigit = "0"
        if len(ds) > 0:
            minDigit = min(ds)
        num.remove(minDigit)
        return int(minDigit + "".join(sorted(num)))