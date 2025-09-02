class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        res = set()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if len({i, j, k}) == 3:
                        x = 100 * digits[i] + 10 * digits[j] + digits[k]
                        if len(str(x)) == 3 and x % 2 == 0:
                            res.add(x)
        return len(res)