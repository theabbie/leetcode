class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        words = {}
        for word in dictionary:
            if len(word) <= len(s):
                i = 0
                j = 0
                while i < len(word) and j < len(s):
                    if word[i] == s[j]:
                        i += 1
                        j += 1
                    else:
                        j += 1
                if i == len(word):
                    words[len(word)] = words.get(len(word), []) + [word]
        if len(words) == 0:
            return ""
        return min(words[max(words.keys())])