class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        n = len(words)
        return [words[i] for i in range(n) if i > 1 and words[i - 1] == second and words[i - 2] == first]