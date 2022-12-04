class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        n = len(sentence)
        for i in range(n):
            if sentence[i] == " ":
                if sentence[i - 1] != sentence[i + 1]:
                    return False
        return sentence[0] == sentence[-1]