class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        bannedWords = set(bannedWords)
        return len([w for w in message if w in bannedWords]) >= 2