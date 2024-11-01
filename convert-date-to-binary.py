class Solution:
    def convertDateToBinary(self, date: str) -> str:
        y, m, d = map(int, date.split("-"))
        b = lambda x: "{:0b}".format(x)
        return f"{b(y)}-{b(m)}-{b(d)}"