class Solution:
    def transform(self, word, i):
        vowels = { 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' }
        op = ""
        if word[0] in vowels:
            op += word + "ma"
        else:
            op += word[1:] + word[0] + "ma"
        op += "a" * i
        return op
    
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        return " ".join([self.transform(word, i+1) for i, word in enumerate(words)])