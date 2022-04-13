class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        words = [word.lower() for word in words]
        words = [(word[0].upper() + word[1:]) if len(word) > 2 else word for word in words]
        return " ".join(words)