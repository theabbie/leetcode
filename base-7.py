class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        sign = ""
        if num < 0:
            sign = "-"
            num *= -1
        op = ""
        while num > 0:
            d = num % 7
            num = num // 7
            op = str(d) + op
        return sign + op