class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        words = []
        i = 0
        for j in range(n):
            if s[j] != " ":
                if j == 0 or s[j - 1] == " ":
                    i = j
                if j == n - 1 or s[j + 1] == " ":
                    words.append(s[i:j+1])
        return " ".join(words[::-1])