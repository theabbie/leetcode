from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ctr = Counter(words)
        longest = 0
        isDouble = False
        for word in list(ctr.keys()):
            if word[0] == word[1]:
                longest += 4 * (ctr[word] // 2)
                rem = ctr[word] % 2
                ctr[word] = rem
                if rem == 1:
                    isDouble = True
            else:
                k = min(ctr[word], ctr[word[::-1]])
                longest += 4 * k
                ctr[word] -= k
                ctr[word[::-1]] -= k
        if isDouble:
            longest += 2
        return longest