class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        comb = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        if len(digits) == 0:
            return []
        words = [c for c in comb[digits[0]]]
        i = 0
        while i < len(words):
            curr = words[i]
            if len(words[i]) == len(digits):
                break
            if len(curr) < len(digits):
                for c in comb[digits[len(curr)]]:
                    words.append(curr + c)
            i += 1
        return words[i:]