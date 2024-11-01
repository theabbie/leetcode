class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if m < n:
            return 0
        pos = lambda c: ord(c) - ord('a')
        tctr = [0] * 26
        for c in word2:
            tctr[pos(c)] += 1
        res = 0
        ctr = [0] * 26
        j = m - 1
        less = 0
        for c in range(26):
            if ctr[c] < tctr[c]:
                less += 1
        for i in range(m - 1, -1, -1):
            ctr[pos(word1[i])] += 1
            if ctr[pos(word1[i])] == tctr[pos(word1[i])]:
                less -= 1
            while j >= i and less + int(ctr[pos(word1[j])] == tctr[pos(word1[j])]) == 0:
                ctr[pos(word1[j])] -= 1
                if ctr[pos(word1[j])] == tctr[pos(word1[j])] - 1:
                    less += 1
                j -= 1
            if less == 0:
                res += m - j
        return res