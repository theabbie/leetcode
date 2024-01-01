class Solution:
    def longest(self, digits, i, n, mod):
        if i >= n:
            if mod != 0:
                return float('-inf')
            return 0
        key = (i, mod)
        if key in self.cache:
            return self.cache[key]
        a = self.longest(digits, i + 1, n, mod)
        b = 1 + self.longest(digits, i + 1, n, (10 * mod + digits[i]) % 3)
        res = max(a, b)
        self.cache[key] = res
        return res
    
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort(reverse = True)
        self.cache = {}
        res = []
        mod = 0
        for i in range(len(digits)):
            if self.longest(digits, i, len(digits), mod) <= 1 + self.longest(digits, i + 1, len(digits), (10 * mod + digits[i]) % 3):
                mod = (10 * mod + digits[i]) % 3
                res.append(str(digits[i]))
        i = 0
        while i < len(res) - 1 and res[i] == "0":
            i += 1
        return "".join(res[i:])