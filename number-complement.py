class Solution:
    def findComplement(self, num: int) -> int:
        return int("".join([str(1 - int(c)) for c in "{:b}".format(num)]), 2)