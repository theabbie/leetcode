class Solution:
    def toMorse(self, s):
        morseMap = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        return "".join([morseMap[ord(c)-ord('a')] for c in s])
    
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len(set([self.toMorse(w) for w in words]))