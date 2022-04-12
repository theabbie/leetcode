class Solution:
    cache = {}

    def maxPalindrome(self, s, i, j):
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        if i == j:
            self.cache[(i, j)] = 1
        elif s[i] == s[j] and i + 1 == j:
            self.cache[(i, j)] = 2
        elif s[i] == s[j]:
            self.cache[(i, j)] = self.maxPalindrome(s, i + 1, j - 1) + 2
        else:
            self.cache[(i, j)] = max(self.maxPalindrome(s, i, j - 1), self.maxPalindrome(s, i + 1, j))
        return self.cache[(i, j)]
    
    def maxProduct(self, s: str) -> int:
        maxP = float('-inf')
        n = len(s)
        for mask in range(1 << n):
            sub = ""
            rest = ""
            for j in range(n):
                if mask & (1 << j):
                    sub += s[j]
                else:
                    rest += s[j]
            if len(sub) > 0 and len(rest) > 0:
                maxP = max(maxP, self.maxPalindrome(sub, 0, len(sub) - 1) * self.maxPalindrome(rest, 0, len(rest) - 1))
        return maxP

s = "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"
print(Solution().maxPalindrome(s, 0, len(s) - 1))