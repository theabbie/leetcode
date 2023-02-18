class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        master.__init__(words[0], words, 1)
        master.guess(words[0])