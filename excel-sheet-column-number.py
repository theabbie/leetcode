class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        for c in columnTitle:
            total = 26 * total + ord(c) - ord('A') + 1
        return total