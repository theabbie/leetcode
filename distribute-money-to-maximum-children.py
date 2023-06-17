class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        money -= children
        res = 0
        for i in range(1, children + 1):
            rem = money - i * 7
            remchildren = children - i
            if rem > 0 and remchildren == 0:
                continue
            if rem >= 0 and (rem != 3 or remchildren != 1):
                res = i
        return res