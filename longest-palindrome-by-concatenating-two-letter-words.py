from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ctr = Counter(words)
        longest = 0
        for word in ctr:
            if word[0] == word[1]:
                longest += 4 * (ctr[word] // 2)
                ctr[word] = ctr[word] % 2
            else:
                if word[::-1] in ctr:
                    if ctr[word] >= ctr[word[::-1]]:
                        longest += 4 * ctr[word[::-1]]
                        ctr[word] -= ctr[word[::-1]]
                        ctr[word[::-1]] = 0
                    else:
                        longest += 4 * ctr[word]
                        ctr[word[::-1]] -= ctr[word]
                        ctr[word] = 0
        for w in ctr:
            if ctr[w] > 0 and w[0] == w[1]:
                longest += 2
                break
        return longest